import os
import csv

def read_csv(filename):
	global path
	global fw
	reader = csv.reader(file(path + filename, 'rb'))
	for line in reader:
		if line[2] == "6212822642" and line[3] == "0" and line[5] == "3":
			# print line[0]
		# if line[2] == "6403444027":
			fw.writelines(str((float(line[0]) - 600000000)/300000000) + "\n")
path = "F:\\data\\task_events\\"
listfile = os.listdir(path)
fw = open("f:\\output\\fail_time\\6212822642_0.txt", "w")
for filename in listfile:
	read_csv(filename)
fw.close()
# read_csv("part-00000-of-00500.csv")
# print len(jobs)
