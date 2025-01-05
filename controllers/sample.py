from controllers import file
from services import drive

def upload_file(service, folders):
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