import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import re
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.metadata.readonly']
service_account_json_key = './config/credentials.json'

def get_mimetype(file_extension):
    """mapping the extension with mime type, for upload"""
    mime_types = {
        'txt': 'text/plain',
        'jpg': 'image/jpeg',
        'png': 'image/png',
        'mov': 'video/quicktime',
        'mp4': 'video/mp4'
    }
    
    ext = file_extension.lower()
    return mime_types.get(ext, mime_types["txt"])

def string_contains_file_extension(text):
    """get file extension too check if this is a file or not, return boolean"""
    # Regular expression for common file extensions
    file_extension_pattern = r'\.(?:txt|jpg|png|mov|mp4|pdf|docx|xlsx)$'
    
    # Search for the pattern in the text
    match = re.search(file_extension_pattern, text, re.IGNORECASE)
    
    return match is not None

def auth():
  """get authentication token using credentials from GCP"""
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(service_account_json_key, SCOPES)
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  service = build("drive", "v3", credentials=creds)
  return service


def get_folders():
  """get the folders and the files and group them"""
  folders_path = os.walk('./testfile')
  items = []
  for root, dirs, files in folders_path:
    f_updated = [f"{root}/{fi}" for fi in files]
    items.append(f_updated + dirs)

  return items

def create_folder(service, folder_name, parent_folder_id=None):
    """Create a folder in Google Drive and return its ID."""
    folder_metadata = {
        'name': folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        'parents': [parent_folder_id] if parent_folder_id else []
    }

    created_folder = service.files().create(
        body=folder_metadata,
        fields='id',
        supportsAllDrives=True
    ).execute()

    print(f'Created Folder ID: {created_folder["id"]}')
    return created_folder["id"]

def upload_file(service, file_path, file_name, mime_type='text/plain', parent_folder_id=None):
  """Upload a file to Google Drive."""
  file_metadata = {
    'name': file_name,
    'parents': [parent_folder_id] if parent_folder_id else []
  }
  media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
  file = service.files().create(
  body=file_metadata, media_body=media, fields='id').execute()
  print(f"Uploaded file with ID: {file.get('id')}")

def main():
  service = auth() # We get the authentication token and service instance for upload
  folders = get_folders() # We get the file & folder group first

  id = ""
  for folder in folders:
    for f in folder:
      """
        if it's a file upload
        if it's a folder create folder
      """
      if string_contains_file_extension(f):
        f_name = f.split('/')[-1]
        f_ext = get_mimetype(f_name.split('.')[-1])
        upload_file(service, f, f_name, f_ext, id)
      else:
        id = create_folder(service, f, id)

if __name__ == "__main__":
  main()