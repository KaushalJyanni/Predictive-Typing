import random
import string
import sys
inp_file = sys.argv[1]
out_file1="t_"+str(inp_file.split("/")[-1])
out_file2="e_"+str(inp_file.split("/")[-1])
# out_file = sys.argv[2]
with open(inp_file,'r') as f:
	data=f.readlines()
totalsize=500
t_setsize=int(0.7*totalsize)
# e_setsize=0.3*totalsize
data=random.sample(data,totalsize)
tdata=data[:t_setsize]
edata=data[t_setsize:]
fdata=[]
for d in tdata:
	newstring=""
	for char in d:
		if char in string.ascii_letters:
			newstring+=char.lower()
		else:
			newstring+=" "
	fdata.append("<s>"+newstring+"</s>\n")

with open(out_file1,'w') as f:
	for s in fdata:
		f.write(s)
fdata=[]
for d in edata:
	newstring=""
	for char in d:
		if char in string.ascii_letters:
			newstring+=char.lower()
		else:
			newstring+=" "
	fdata.append("<s>"+newstring+"</s>\n")

with open(out_file2,'w') as f:
	for s in fdata:
		f.write(s)