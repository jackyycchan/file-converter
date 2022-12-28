import os
import sys

srcDir = "src/"
distDir = "dist/"

for path in os.listdir(srcDir):
    with open(srcDir + path, 'rb') as file:
        # Read the contents of the file into a binary string in bytes
        binary_string_in_bytes = file.read()

    # convert to binary string
    binary_string = bin(int.from_bytes(binary_string_in_bytes, byteorder=sys.byteorder))
    print(path)

    # reverse to bytes
    binary_string_in_int = int(binary_string, 2)
    converted_binary_string_in_bytes = binary_string_in_int.to_bytes((binary_string_in_int.bit_length() + 7) // 8, byteorder=sys.byteorder)
    
    # Open a new file in binary mode
    with open(distDir + path, 'wb') as file:
        # Write the binary string in bytes to the file
        file.write(converted_binary_string_in_bytes)