import os
import sys

srcDir = "src/"
distDir = "dist/"

def convertToBinaryString(bytesContent):
    return bin(int.from_bytes(bytesContent, byteorder=sys.byteorder))

for path in os.listdir(srcDir):
    if path == ".DS_Store":
        continue

    # try:
    with open(srcDir + path, 'rb') as file:
        counter = 0

        while True:
            # Read the contents of the file into a binary string in bytes
            binary_string_in_bytes = file.read(200000000) #200MB

            if not binary_string_in_bytes:
                break

            # turn into binary string
            binary_string = convertToBinaryString(binary_string_in_bytes)

            # reverse to bytes
            binary_string_in_int = int(binary_string, 2)
            converted_binary_string_in_bytes = binary_string_in_int.to_bytes((binary_string_in_int.bit_length() + 7) // 8, byteorder=sys.byteorder)
        
            # write file
            distPath = distDir + path.replace(".", "_") + "_{}.bin".format(str(counter))
            with open(distPath, "w") as wFile:
                wFile.write(converted_binary_string_in_bytes)

            print(distPath)
            counter+=1
        
    # except:
    #     print("err occur")


# open file
# if read file != empty string ~20MB
# write file
