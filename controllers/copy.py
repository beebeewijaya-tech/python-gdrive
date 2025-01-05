from services import drive

def loop_through_files_upload(service, parent_folder_id, new_parent_folder_id):
  listFiles = drive.list_files_from_parent_folder(service, parent_folder_id)

  for f in listFiles:
    isFolder = f["mimeType"] == "application/vnd.google-apps.folder"
    if isFolder:
      id = drive.create_folder(service, f["name"], new_parent_folder_id)
      loop_through_files_upload(service, f["id"], id)
    else:
      f_id = f["id"]
      f_name = f["name"]
      drive.copy_file(service, f_id, f_name, new_parent_folder_id)