import sys

fastaFile = open(sys.argv[1], "r")
org = sys.argv[1].split(".")[0]
print (org)
parsed = open(org+".txt", "+w")

seq = fastaFile.read().split("\n\n") #indiv sequences with header
for i in range (0, len(seq)-1): #iterate on each sequences
	header = seq[i].split("\n")[0]
	header = header.split("|")
	
	parsed.write(header[3] + "|" + header[1] + "|" + header[4] + "|") #id | genbankid | protein name |
	parsed.write(''.join(seq[i].split("\n")[1:]) + "|" + org + "|\n") #sequence | type (PHATR/THAPS/THAOC)

fastaFile.close()
parsed.close()