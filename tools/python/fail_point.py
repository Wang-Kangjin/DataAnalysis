import os
import csv
import math

def read(failfile, tsfile):
	global path2
	global path
	f = open(path + failfile, "r")
	fw = open("f:\\task\\fail_1_evictpoints\\" + failfile, "w")
	# fw2 = open("f:\\task\\fail_1_runpoints\\" + failfile, "w")
	lines = f.readlines()
	fail_times = []
	for line in lines:
		if line != "\n":
			fail_times.append(int(math.floor(float(line.strip()))))
	csvReader = csv.reader(file(path2 + tsfile))
	for line in csvReader:
		if int(line[0]) in fail_times:
			fw.writelines(line[0] + "\t" + line[5] + "\t" + line[6] + "\n")
		# else:
		# 	fw2.writelines(line[0] + "\t" + line[5] + "\t" + line[6] + "\n")
	fw.close()
	# fw2.close()
	f.close()


path = "f:\\task\\fail_1_evicttime\\"
path2 = "f:\\task\\fail_1_ts\\"
listfile = os.listdir(path)
for filename in listfile:
	words = filename[0:len(filename)-4].split('-')
	job = words[0]
	task = words[1]
	read(filename, "fail1-" + job + "-" + task + ".csv")