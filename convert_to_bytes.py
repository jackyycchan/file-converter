import os
import sys
import re

def get_original_file_name(fileName):
    # Remove ".bin" suffix
    fileName = fileName.replace(".txt", "")

    # Find the last index of "-"
    last_dash_index = fileName.rindex("-")

    # Replace the last "-" with "."
    fileName = fileName[:last_dash_index] + "." + fileName[last_dash_index+1:]

    return fileName

def read(path):
    with open(path, 'rb') as file:
        # Read the contents of the binary file
        contents_in_bytes = file.read()

    return contents_in_bytes

def write(content, path):
    try:        
        # Open a new file in binary mode
        with open(path, 'wb') as file:
            # Write the binary string in bytes to the file
            file.write(content)
    except Exception as e:
        print('[Write] An error occurred:', e)
        exit()

baseDir = os.path.join("resources", "dest")
srcDir = "bin"
destDir = "bytes"

if not os.path.exists(os.path.join(baseDir, srcDir)):
    os.makedirs(os.path.join(baseDir, srcDir))

if not os.path.exists(os.path.join(baseDir, destDir)):
    os.makedirs(os.path.join(baseDir, destDir))

for path in os.listdir(os.path.join(baseDir, srcDir)):
    # exclud op specific files, e.g. .DS_Store for macOS
    if path == ".DS_Store":
        continue

    try:
        contents_in_bytes = read(os.path.join(baseDir, srcDir, path))
    except Exception as e:
        print('[Read] An error occurred:', e)
        exit()

    # Add '0b' prefix
    contents_in_str = '0b' + contents_in_bytes.decode()
    # Convert into integer
    contents_in_int = int(contents_in_str, 2)

    # get original file name from generated file, e.g: abc-txt.txt -> abc.txt
    write(contents_in_int.to_bytes((contents_in_int.bit_length() + 7) // 8, byteorder=sys.byteorder), os.path.join(baseDir, destDir, get_original_file_name(path)))
    
exit()