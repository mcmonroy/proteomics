-- manual pa ang pagcreate ng db sa sql

-- CREATE DATABASE IF NOT EXISTS proteomics;


CREATE TABLE IF NOT EXISTS PROTEINS (
	seq_id varchar(50) NOT NULL PRIMARY KEY,
	genbank_id TEXT(50) NOT NULL,
	protein_name TEXT(200) NOT NULL,
	sequence TEXT(500) NOT NULL,
	type TEXT(20) NOT NULL,
	rbh TEXT(50) NOT NULL
	-- no_seq_chars INTEGER
);


LOAD DATA LOCAL INFILE './shortTHAPS.txt' INTO TABLE PROTEINS
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n';