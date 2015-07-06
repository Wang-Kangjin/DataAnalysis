import os
import csv

def read_csv(filename):
	global path
	global tasks
	reader = csv.reader(file(path + filename, 'rb'))
	job = "3998246386"
	task = "0"
	count = 0
	output_lines=[]
	for line in reader:
		# for task in tasks:
		# 	words = task.split(',')
			# job = words[0]
			# task = words[1]
			if line[2] == job and line[3] == task and line[5] == "3":
				line[0] = (float(line[0]) - 600000000))/300000000
				print ','.join(line)
				# fw = open("f:\\task\\fail_time_top10\\" + job + "_" + task + ".txt", "a")
				# fw.writelines(str((float(line[0]) - 600000000)/300000000) + "\n\n")
				# fw.close()

path = "f:\\task_events\\"
listfile = os.listdir(path)
# f = csv.reader(file("f:\\500_targetjob.csv", "rb"))
# tasks = []
# for line in f:
# 	tasks.append(line[0] + ',' + line[1])

for filename in listfile:
	print filename
	read_csv(filename)
# f.close()
