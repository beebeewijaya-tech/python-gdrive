import sys
import os

from controllers import auth, file, sample, copy, download
from services import drive

def main():
  n = len(sys.argv)
  if n != 2:
    raise Exception("please use 2 arguments, source folder and destination")

  source = sys.argv[1]
  service = auth.auth() # We get the authentication token and service instance for upload

  os.mkdir(source)
  parentFolder = drive.search_folder_name(service, source)[0]["id"]
  download.loop_through_files_download(service, parentFolder, source)


if __name__ == "__main__":
  main()