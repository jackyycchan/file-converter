MAP_DNA_DICT = {
	"00" : "A",
	"01" : "C",
	"10" : "G",
	"11" : "T"
}

def get_digits_from_dna(dna):
	for key, value in MAP_DNA_DICT.items():
		if value == dna:
			return key
	return ""

def get_original_file_name(file_name):
	# Remove ".bin" suffix
	file_name = file_name.replace(".txt", "")

	# Find the last index of "-"
	last_dash_index = file_name.rindex("-")

	# Replace the last "-" with "."
	file_name = file_name[:last_dash_index] + "." + file_name[last_dash_index+1:]

	return file_name

def read(path, mode):
	try:
		with open(path, mode) as file:
			# Read the contents of the file into a binary string in bytes 
			contents_in_bytes = file.read()

		return contents_in_bytes
	except Exception as e:
		print('[Read] An error occurred:', e)
		exit()

def write(content, path, mode):
	try:
		# Open a file for writing binary data
		with open(path, mode) as file:
			file.write(content)
	except FileNotFoundError as e:
		print('[Write] File does not exist:', e)
		exit()
	except Exception as e:
		print('[Write] An error occurred:', e)
		exit()