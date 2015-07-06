import os
import csv

def read_csv(filename):
	global path
	global fw
	reader = csv.reader(file(path + filename, 'rb'))
	print "processing " + filename
	for line in reader:
		curr_job_id = line[2]
		curr_task_id = line[3]
		curr_event = line[5]
		if curr_event == "3":
			if curr_job_id in target_task and curr_task_id == target_task[curr_job_id]:
				with open(curr_job_id+"_"+curr_task_id+".txt", 'a') as writefile :
					writefile.write(str((float(line[0]) - 600000000)/300000000) + "\n")
	print "prosses " + filename +" end"

path = "F:\\data\\task_events\\"
target_task={}

def read_config():
	global target_task
	with open("F:\\output\\etc\\fail_1_time_top100.csv") as conf_file:
		conf_reader = csv.reader(conf_file)
		for line in conf_reader:
			job_id = line[0]
			task_id = line[1]
			target_task[job_id+"#"+task_id] = task_id


def main():
	read_config()
	listfile = os.listdir(path)
	#fw = open("f:\\task\\fail_time\\6316376261_0.txt", "w")
	for filename in listfile:
		read_csv(filename)
	

if __name__ == '__main__':
	main()