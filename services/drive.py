from googleapiclient.http import MediaFileUpload

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

def search_folder_name(service, folder_name):
  results = (
        service.files()
        .list(pageSize=100, fields="nextPageToken, files(id, name, mimeType)", q=f'name = "{folder_name}"')
        .execute()
  )
  items = results.get("files", [])
  return items

def search_folder_name(service, folder_name):
  results = (
        service.files()
        .list(pageSize=100, fields="nextPageToken, files(id, name, mimeType)", q=f'name = "{folder_name}" and mimeType = "application/vnd.google-apps.folder"')
        .execute()
  )
  items = results.get("files", [])
  return items

def list_files_from_parent_folder(service, parent_folder_id):
  results = (
        service.files()
        .list(pageSize=100, fields="nextPageToken, files(id, name, mimeType)", q=f'"{parent_folder_id}" in parents')
        .execute()
  )
  items = results.get("files", [])
  return items


def copy_file(service, fileId, fileName, parent_folder_id):
  newFile = {"parents": [parent_folder_id], 'name': fileName}
  service.files().copy(fileId=fileId, body=newFile).execute()
  print(f"Copying {fileId}-{fileName} into new parent {parent_folder_id}")