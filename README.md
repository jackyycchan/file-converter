# File transformer
This is a demo for transforming file into binary string and reverse back to corresponding file format using python

# Prerequisite
- Python 3.0.0+

# Usage
- Place all target files into **src/** directory
- Follow below steps in order to generate corresponding files under **resources/dest/** directory:
1. Convert src files into binary text file
	```SELinux
	> python convert_to_bin.py
	```
	All files locating in **src/** directory will be converted into binary
	All output file will be located at **bin/**

2. Convert binary text file into DNA sequence
	```SELinux
	> python convert_to_dna.py
	```
	All output file will be located at **dna/**

3. Reverse DNA sequence into original file
	```SELinux
	> python reverse_to_original_enhance.py
	```
	All output file will be located at **bytes/**

# Limitations
- Memory-intensive
- Not support splits on output files
- Not support only run on single file
- Mapping between DNA and bits is not dynamic
