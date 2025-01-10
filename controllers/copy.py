import time
import random

def loop_through_files_upload(drive, parent_folder_id, new_parent_folder_id):
  listFiles = drive.list_files_from_parent_folder(parent_folder_id)

  for f in listFiles:
    duration = random.uniform(1.5, 3.0)

    isFolder = f["mimeType"] == "application/vnd.google-apps.folder"
    if isFolder:
      id = drive.create_folder(f["name"], new_parent_folder_id)
      loop_through_files_upload(drive, f["id"], id)
    else:
      f_id = f["id"]
      f_name = f["name"]
      drive.copy_file(f_id, f_name, new_parent_folder_id)

    time.sleep(duration)
