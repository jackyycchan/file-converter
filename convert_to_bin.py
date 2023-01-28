import os
import sys

# custom
from common import read, write

resDir  = "resources"
srcDir  = "src"
destDir = os.path.join("dest", "bin")

if not os.path.exists(os.path.join(resDir, srcDir)):
    os.makedirs(os.path.join(resDir, srcDir))

if not os.path.exists(os.path.join(resDir, destDir)):
    os.makedirs(os.path.join(resDir, destDir))


for path in os.listdir(os.path.join(resDir, srcDir)):
    # exclud op specific files, e.g. .DS_Store for macOS
    if path == ".DS_Store":
        continue

    contents_in_bytes = read(os.path.join(resDir, srcDir, path), 'rb')

    # Convert to binary string
    binary_string = bin(int.from_bytes(contents_in_bytes, byteorder=sys.byteorder))
    # Remove the '0b' prefix from the binary string
    binary_string = binary_string.lstrip('0b')

    # Encode the string to bytes
    write(binary_string.encode(), os.path.join(resDir, destDir, path.replace(".", "-") + ".txt"), 'wb')

exit()


