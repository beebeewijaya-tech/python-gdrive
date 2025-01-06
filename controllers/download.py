from services import drive
import os

def loop_through_files_download(service, parent_folder_id, folder):
  listFiles = drive.list_files_from_parent_folder(service, parent_folder_id)

  for f in listFiles:
    isFolder = f["mimeType"] == "application/vnd.google-apps.folder"
    if isFolder:
      fName = os.path.join(folder, f["name"])
      print(f, fName)
      if not os.path.exists(fName):
        os.mkdir(fName)
      loop_through_files_download(service, f["id"], fName)
    else:
      print(f)
      drive.downloadfiles(service, f["id"], f["name"], folder)