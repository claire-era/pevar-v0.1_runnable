import collections
print("********************************************************************************************************************")
print("\n\t\t\t\t\tPEVAR: Automated Pedigree Verification\n")
print("\t\t\t\t\t\t---- RESULTS-----\n")
fname = "results.log"

# percent100_count = 0
data_err_count = 0
grpcount=0
tp = 0
tn = 0
fp = 0
fn = 0


verdict = {}

# key = ""
with open(fname, "r") as f:
	for line in f:
		if(".hmp.txt" in line):
			key = line.split(".hmp.txt")[0].split(" ")[1]
			grpcount+=1

		if ("DATA_ERR" in line):
			data_err_count+=1

		if("TP" in line):
			# print(line,sep="")
			tp = int(line.split(" ")[0].split("TP:")[1])
			tn = int(line.split(" ")[1].split("TN:")[1])
			fp = int(line.split(" ")[2].split("FP:")[1])
			fn = int(line.split(" ")[3].split("FN:")[1])
			totalsamplesingrp = tp + tn + fp + fn
			# print(totalsamplesingrp)
			if((tp+fn)==0 or (tp+fp==0)):
				verdict[key] = ['N/A','N/A']
			else:
				verdict[key] = [(tp/(tp+fn)),(tp/(tp+fp))]



for k in verdict:
	print(k, "REPORT ")
	if(verdict[k][0] == "N/A"):
		print("RECALL: N/A")
	if(verdict[k][1] == "N/A"):
		print("PRECISION: N/A")
	else:
		print("RECALL: ", '%.3f'%(float((verdict[k][0]*100))), "%")
		print("PRECISION: ", '%.3f'%(float((verdict[k][1]*100))), "%")
	print("\n")

print("*********")
# print("\t\t\t\t\t100% SAMPLE MATCH: ", (percent100_count), "(",'%.3f'%(float((percent100_count/grpcount))*100),"%)")
print("DATA ERRORS: ", (data_err_count), "(",'%.3f'%(float((data_err_count/grpcount))*100),"%)")
print("*********")
# od = collections.OrderedDict(sorted(percent.items()))
# for k, v in od.items():
# 	print("\t\t\t\t\t",k, "% match: ", v, "sample/s", "(",'%.3f'%(float((v/grpcount))*100),"%)")
print("TOTAL NO. OF F1 GROUPS: ", (grpcount))
print("*********")








# # Identify by True positives, False Negatives, True Negatives and False Positives.
# 										MANUAL:AUTO
# TP= true sa manual, true sa matic			1:1
# TN= false sa manual, false sa matic			0:0
# FP= false sa manual, true sa matic			0:1
# FN= true sa manual, false sa matic			1:0

# # get recall and precision:
# # recall = tp / (tp + fn)
# # precision = tp / (tp + fp)