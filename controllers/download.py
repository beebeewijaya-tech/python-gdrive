import os
import time
import random

def loop_through_files_download(drive, parent_folder_id, folder):
  listFiles = drive.list_files_from_parent_folder(parent_folder_id)

  for f in listFiles:
    duration = random.uniform(1.5, 3.0)
    isFolder = f["mimeType"] == "application/vnd.google-apps.folder"
    if isFolder:
      fName = os.path.join(folder, f["name"])
      print(f, fName)
      if not os.path.exists(fName):
        os.mkdir(fName)
      loop_through_files_download(drive, f["id"], fName)
    else:
      print(f)
      drive.downloadfiles(f["id"], f["name"], folder)

    time.sleep(duration)