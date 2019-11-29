import sys

org = sys.argv[1]

sqlfile = open("import.sql", "+a")

sqlfile.write("CREATE TABLE IF NOT EXISTS " + proteins + " (\n")
sqlfile.write("\tseq_id TEXT NOT NULL PRIMARY KEY,\n")
sqlfile.write("\tgenbank_id TEXT NOT NULL,\n")
sqlfile.write("\tprotein_name TEXT NOT NULL,\n")
sqlfile.write("\ttype TEXT NOT NULL,\n")
# sqlfile.write("\trbh TEXT NOT NULL,\n")
sqlfile.write("\t-- no_seq_chars INTEGER\n);\n")

sqlfile.close()
