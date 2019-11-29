import sys

consprofFile = open(sys.argv[1], "r")
org = sys.argv[1].split("_")[0]
print (org)
parsed = open(org+".txt", "+w")

cons = consprofFile.read().split("\n")  #per row
for i in range (1, len(cons)-1): 
	data = cons[i].split("\t")
	ident = data[0].split("|")[3]
	
	if data[1] != "0":
		xy = data[1].split("|")[3]
	else:
		xy = "0"
	
	
	if data[2] != "0":
		xz = data[2].split("|")[3]
	else:
		xz = "0"

	parsed.write(ident + "|" + xy + "|" + xz + "|\n")
consprofFile.close()
parsed.close()