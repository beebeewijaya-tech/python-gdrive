## Project Introduction
I want to explore on what does the GDrive API could do.

Several things I implements on this project
- Upload files
- Create folder
- List Files / Folders
- Duplicate folder into new folder ( Combining all of 3 above )


## Setup
Running this project require

1. config/credentials.json
2. testfile/please-upload-your-file
3. If you want to duplicate, prepare your folder name that you wanted to duplicate.

## How to run
if all been set

```
  python3 -m venv venv
  pip3 install requirements.txt
  python3 main.py source_folder_name destination_folder_name
```