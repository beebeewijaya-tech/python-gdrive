import os
import re

def get_folders():
  """get the folders and the files and group them"""
  folders_path = os.walk('./testfile')
  items = []
  for root, dirs, files in folders_path:
    f_updated = [f"{root}/{fi}" for fi in files]
    items.append(f_updated + dirs)

  return items


def get_mimetype(file_extension):
    """mapping the extension with mime type, for upload"""
    mime_types = {
        'txt': 'text/plain',
        'jpg': 'image/jpeg',
        'png': 'image/png',
        'mov': 'video/quicktime',
        'mp4': 'video/mp4'
    }
    
    ext = file_extension.lower()
    return mime_types.get(ext, mime_types["txt"])

def string_contains_file_extension(text):
    """get file extension too check if this is a file or not, return boolean"""
    # Regular expression for common file extensions
    file_extension_pattern = r'\.(?:txt|jpg|png|mov|mp4|pdf|docx|xlsx)$'
    
    # Search for the pattern in the text
    match = re.search(file_extension_pattern, text, re.IGNORECASE)
    
    return match is not None