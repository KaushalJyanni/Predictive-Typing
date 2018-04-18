import random
import string
import sys
inp_file = sys.argv[1]
out_file = sys.argv[2]
with open(inp_file,'r') as f:
	data=f.readlines()

data=random.sample(data,500)
fdata=[]
for d in data:
	newstring=""
	for char in d:
		if char in string.ascii_letters:
			newstring+=char.lower()
		else:
			newstring+=" "
	fdata.append("<s>"+newstring+"</s>\n")

with open(out_file,'w') as f:
	for s in fdata:
		f.write(s)