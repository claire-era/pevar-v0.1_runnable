#RUN ONCE: CLEAR CONTENTS OF DATAFRAME.hmp.txt to avoid errors
#program only works on sorted hmp.txt. FILES

import csv
import os

def getGroups(alltaxa, germplasm_map):
	#GET ONLY GROUPS THAT ARE 'F1' IN germplasm_map
	# print(len(germplasm_map), len(alltaxa))
	samples = []
	for i in range(0,len(alltaxa)):
		if germplasm_map[i][2] == "F1":#choose only groups that have germplasm_type: F1.
			samples.append(alltaxa[i].rsplit("-", 1)[0])

	d = {x:samples.count(x) for x in samples} #https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list/2162045
	return d

def readClassificationFile(file):
	germplasm_mapping_to_type = []
	i = 0 
	with open(file,"r") as f:
		line = f.readline()#ignore first line. this indicates subject+id, score, germplasm_type respectively
		reader = csv.reader(f, dialect='excel', delimiter="\t")
		for row in reader:
			germplasm_mapping_to_type.append(row)

	return germplasm_mapping_to_type


def createDataframe(file, germplasm_map):
	i = 0;
	allrows = []
	with open(file, "r") as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		for row in reader:
			# allrows.append(row)
			# print(row[11:12])
			if i == 0: #read all taxa
				alltaxa = row[11:]
				taxagrp_F1_count = getGroups(alltaxa, germplasm_map)
				i = i + 1
			crow = row[:11]
			o = open(out, "a")
			for word in crow:
				o.write(str(word) + "\t")
			o.write("\n")
	o.close()
	
	# print(len(taxagrp_F1_count))
	taxaCountAllGroups = 0
	for e in taxagrp_F1_count.keys():	
		taxaCountAllGroups  = taxaCountAllGroups + taxagrp_F1_count[e]
	# print(count)
	taxamap = [taxagrp_F1_count,  taxaCountAllGroups, alltaxa, allrows]
	return taxamap

def getCol(hmpfile, germplasm_map):
	# alltaxa = taxamap_F1_alltaxa[1]
	allcol=[]
	init = 11
	allrows = [] 

	with open(hmpfile, "r") as f:
		reader = csv.reader(f, dialect='excel', delimiter='\t')
		for row in reader:
			allrows.append(row)


	for j in range(0,len(germplasm_map)+init): #add offset of 11 to accomodate 11 rows of hapmap file
		taxaseq = ""		
		for row in allrows:
			taxaseq += str(row[j:j+1][0]) + "\t"
		taxaseq=taxaseq[:-1]	
		allcol.append(taxaseq)

	return allcol

def appendToDataframe(taxamap_F1_alltaxa, allcol):
	taxagrp_F1_count = taxamap_F1_alltaxa[0]
	df = "DATAFRAME.hmp.txt"
	# os.mkdir('hmp_files_f1/')
	
	c=0
	for grp in taxagrp_F1_count.keys():
		sequence = []
		for c in range(0,taxagrp_F1_count[grp]-1):
			s=[]
			for g in allcol:
				if grp in g:
					l = g.split("\t")
					s.append(l[c])
			
			#convert list s to string and put inside file	
			seq=""
			for word in s:
				seq+=word+"\t"
			sequence.append(seq)


		#add to file.
		j=0
		with open(df,"r") as inf:
			with open(grp + ".hmp.txt", "w") as outf:
				for line in inf:
					if j < len(sequence):
						line = line.rstrip('\n') + sequence[j]
						line=line[:-1]
						j+=1
						print(line, file=outf)

############## MAIN ##############
#FILES NEEDED
hmp_file = "whole_snp_seq.hmp.txt"
data_file = "data_information.txt"

out = "DATAFRAME.hmp.txt" #skeleton file for snp files

#STORE DATA_CLASSIFICATION CONTENTS 
germplasm_map = readClassificationFile(data_file)
taxamap_F1_alltaxa = createDataframe(hmp_file, germplasm_map) #creates a data frame. kindly delete the dataframe when running again
allcol = getCol(hmp_file, germplasm_map)
appendToDataframe(taxamap_F1_alltaxa, allcol) #passthe taxagrp_f1_count

#https://stackoverflow.com/questions/25923186/append-text-single-letter-to-the-end-of-each-line-in-a-text-file


