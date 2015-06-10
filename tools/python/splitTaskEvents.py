#!/usr/bin/env python

#Auther : wangkangjin
#create time 2015-06-10
#Split 500 task_events csv-files to individual file group by job_id and task_index
import csv
import glob

data_path = "/home/kangjin/data/task_events/"
output_path = "~/data/ouput/"
output_prefix = "task_events_"
csv_files_globbing = "part-*.csv"

def splite(one_file):
	with open(one_file) as csv_file:
		csv_reader = csv.reader(csv_file)
		for line in csv_reader:
			#type of line is list
			job_id = line[2]
			task_index = line[3]
			splite_file = open(output_path+output_prefix+job_id+"_"+task_index,'a')
			write_line = ','.join(line)a
			splite_file.write(write_line)

def main():
	data_files = glob.glob(data_path+csv_files_globbing)
	for one_file in data_files:
		splite(one_file)

if __name__ == '__main__':
	main()