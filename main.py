from controllers import auth, file
from services import drive

def main():
  service = auth.auth() # We get the authentication token and service instance for upload
  folders = file.get_folders() # We get the file & folder group first

  id = ""
  for folder in folders:
    for f in folder:
      """
        if it's a file upload
        if it's a folder create folder
      """
      if file.string_contains_file_extension(f):
        f_name = f.split('/')[-1]
        f_ext = file.get_mimetype(f_name.split('.')[-1])
        drive.upload_file(service, f, f_name, f_ext, id)
      else:
        id = drive.create_folder(service, f, id)

if __name__ == "__main__":
  main()