import os

from common import read, write, MAP_DNA_DICT

# config
isMapping = True

baseDir = os.path.join("resources", "dest")
srcDir = "bin"
destDir = "bin-ls" if not isMapping else "dna"

if not os.path.exists(os.path.join(baseDir, destDir)):
    os.makedirs(os.path.join(baseDir, destDir))

for path in os.listdir(os.path.join(baseDir, srcDir)):
	# exclud op specific files, e.g. .DS_Store for macOS
	if path == ".DS_Store":
		continue

	contents_in_str = read(os.path.join(baseDir, srcDir, path), 'r')

	contents_to_file = ""
	for index in range(0, len(contents_in_str) - 1, 2):
		target = contents_in_str[index:index+2]

		if isMapping:
			contents_to_file += MAP_DNA_DICT[target]
		else:
			contents_to_file += target + '\n'

	write(contents_to_file, os.path.join(baseDir, destDir, path) , 'w')
