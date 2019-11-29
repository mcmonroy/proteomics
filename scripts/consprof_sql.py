import sys

consprofFile = open(sys.argv[1], "r")
org = sys.argv[1].split("_")[0]
print (org)
parsed = open(org+".txt", "+w")

cons = consprofFile.read().split("\n") #indiv sequences with header
for i in range (1, len(cons)-2): #iterate on each sequences
	rbh = []
	data = cons[i].split("\t")
	ident = data[0].split("|")[3]
	#print(data[1])
	
	if data[1] != "0":
		xy = data[1].split("|")[3]
	else:
		xy = "0"
	
	
	if data[2] != "0":
		xz = data[2].split("|")[3]
	else:
		xz = "0"

	#rbh.append(xy)
	#rbh.append(xz)

	#parsed.write(ident + "|" + str(rbh) + "|\n")
	parsed.write(ident + "|" + xy + "|" + xz + "|\n")
consprofFile.close()
parsed.close()