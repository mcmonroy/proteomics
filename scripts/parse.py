import sys
import os

fastaFile = open(sys.argv[1], "r")
org = (sys.argv[1].split(".")[0])

# os.system("mkdir -p "+org+" || exit 1")
parsed = open((org + "/" + org + ".pep"), "+w")
	

seq = fastaFile.read().split("\n\n") #indiv sequences with header
for i in range (0, len(seq)):
	header = seq[i].split("\n")[0]

	parsed.write(">" +  (header.split("|"))[3] + "\n") #remove identifier, starts with ID in writing
	parsed.write('\n'.join(seq[i].split("\n")[1:]) + "\n\n") #sequence


fastaFile.close()
parsed.close()

