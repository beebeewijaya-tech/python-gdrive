import sys
import os

from controllers import auth, file, sample, copy, download
from services.drive import DriveService

def main():
  n = len(sys.argv)
  if n != 2:
    raise Exception("please use 2 arguments, source folder and destination")

  source = sys.argv[1]
  service = auth.auth() # We get the authentication token and service instance for upload

  drive = DriveService(service)

  if not os.path.exists(source):
    os.mkdir(source)
  parentFolder = drive.search_folder_name(source)[0]["id"]
  download.loop_through_files_download(drive, parentFolder, source)


if __name__ == "__main__":
  main()