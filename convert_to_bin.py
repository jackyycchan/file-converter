import os
import sys

resDir  = "resources"
srcDir  = "src"
destDir = os.path.join("dest", "bin")

if not os.path.exists(os.path.join(resDir, srcDir)):
    os.makedirs(os.path.join(resDir, srcDir))

if not os.path.exists(os.path.join(resDir, destDir)):
    os.makedirs(os.path.join(resDir, destDir))

def read(path):
    with open(path, 'rb') as file:
        # Read the contents of the file into a binary string in bytes 
        contents_in_bytes = file.read()

    return contents_in_bytes


def write(content, path):
    try:
        # Open a file for writing binary data
        with open(path, 'wb') as file:
            file.write(content)
    except FileNotFoundError as e:
        print('[Write] File does not exist:', e)
        exit()
    except Exception as e:
        print('[Write] An error occurred:', e)
        exit()


for path in os.listdir(os.path.join(resDir, srcDir)):
    # exclud op specific files, e.g. .DS_Store for macOS
    if path == ".DS_Store":
        continue

    try:
        contents_in_bytes = read(os.path.join(resDir, srcDir, path))
    except Exception as e:
        print('[Read] An error occurred:', e)
        exit()

    # Convert to binary string
    binary_string = bin(int.from_bytes(contents_in_bytes, byteorder=sys.byteorder))
    # Remove the '0b' prefix from the binary string
    binary_string = binary_string.lstrip('0b')

    # Encode the string to bytes
    write(binary_string.encode(), os.path.join(resDir, destDir, path.replace(".", "-") + ".txt"))

exit()


