import os
import sys
import re

# custom
from common import read, write, get_original_file_name, get_digits_from_dna

baseDir = os.path.join("resources", "dest")
srcDir = "dna"
destDir = "bytes"

if not os.path.exists(os.path.join(baseDir, srcDir)):
    os.makedirs(os.path.join(baseDir, srcDir))

if not os.path.exists(os.path.join(baseDir, destDir)):
    os.makedirs(os.path.join(baseDir, destDir))

for path in os.listdir(os.path.join(baseDir, srcDir)):
    print(path)

    # exclud op specific files, e.g. .DS_Store for macOS
    if path == ".DS_Store":
        continue

    # read contents, e.g "ACGTTTAAA"
    contents_in_bytes = read(os.path.join(baseDir, srcDir, path), 'r')

    # translate to "10110111"
    contents_in_str = ""
    for dna in contents_in_bytes:
        contents_in_str += get_digits_from_dna(dna)

    # Add '0b' prefix and Convert into integer
    contents_in_int = int("0b" + contents_in_str, 2)

    # get original file name from generated file, e.g: abc-txt.txt -> abc.txt
    write(contents_in_int.to_bytes((contents_in_int.bit_length() + 7) // 8, byteorder=sys.byteorder), os.path.join(baseDir, destDir, get_original_file_name(path)), 'wb')

exit()