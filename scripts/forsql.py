import sys

fastaFile = open(sys.argv[1], "r")
parsed = open("THAPSdb.txt", "+w")

seq = fastaFile.read().split("\n\n") #indiv sequences with header
for i in range (0, len(seq)): #iterate on each sequences
	header = seq[i].split("\n")[0]

	parsed.write('|'.join((header.split("|"))[3:]) + "|") #remove identifier, starts with ID in writing
	parsed.write(''.join(seq[i].split("\n")[1:]) + "|\n")

fastaFile.close()
parsed.close()
