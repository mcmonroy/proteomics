import sys
import os

fastaFile = open("../proteins/"+sys.argv[1], "r")
org = (sys.argv[1].split(".")[0])


seq = fastaFile.read().split("\n\n") #indiv sequences with header
for i in range (0, len(seq)): #iterate on each sequences
	header = seq[i].split("\n")[0]

	# parsed = os.open((header.split("|")[3]+".faa"), os.O_WRONLY, 0o600)
	parsed = open((header.split("|")[3]+".faa"), "w+")
	parsed.write('|'.join((header.split("|"))[3:]) + "\n") #remove identifier, starts with ID in writing
	parsed.write('\n'.join(seq[i].split("\n")[1:]) + "\n")


fastaFile.close()
parsed.close()