import sys

from controllers import auth, file, sample, copy
from services import drive


def main():
  n = len(sys.argv)
  if n != 3:
    raise Exception("please use 2 arguments, source folder and destination")

  source = sys.argv[1]
  destination = sys.argv[2]

  service = auth.auth() # We get the authentication token and service instance for upload

  parentFolder = drive.search_folder_name(service, source)[0]["id"]
  newParent = drive.create_folder(service, destination)
  copy.loop_through_files_upload(service, parentFolder, newParent)

if __name__ == "__main__":
  main()