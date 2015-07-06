#!/usr/bin/env python

#Auther : wangkangjin
#create time 2015-06-10
#Split 500 task_events csv-files to individual file group by job_id and task_index
import csv
import glob

data_path = "F:\\data\\"+ "task_events\\"
#data_path = Config.my_data_path + "test/"
output_path = "F:\\data\output\\splite_task_events\\" + "task_attribute.csv"
csv_files_globbing = "part-*.csv"

#key is job_id+task_id+machine_id
job_dict = {}

sc_change = False
priority_change = False
rcpu_change = False
rmem_change = False
rdisk_change = False

def deal(one_file):
	print "processing "+one_file
	with open(one_file) as csv_file:
		csv_reader = csv.reader(csv_file)
		for line in csv_reader:
			#type of line is list
			job_id 			 = line[2]
			task_index 		 = line[3]
			machine_id		 = line[4]
			event_type		 = line[5]
			username 		 = line[6]
			scheduling_class = line[7]
			priority 		 = line[8]
			req_cpu  		 = line[9]
			req_mem			 = line[10]
			req_space		 = line[11]
			diff_machine	 = line[12]
			fail_times = '0'
			end_statue = event_type
			dict_item = [
						job_id,
						task_index,
						machine_id,
						username,
						scheduling_class,
						priority,
						req_cpu,
						req_mem,
						req_space,
						diff_machine,
						str(fail_times),
						end_statue 
						]
			key = job_id+task_index+machine_id
			if key not in job_dict:
				if event_type == '3':
					fail_times = '1'
				dict_item[10] = fail_times
				job_dict[key] = dict_item
			else:
				if event_type == '3':
					job_dict[key][10] = str( long(job_dict[key][10]) + 1)
				job_dict[key][11] = event_type
				update_change(key, dict_item)

def update_change(key, dict_item):
	global sc_change
	global priority_change
	global rcpu_change
	global rmem_change
	global rdisk_change
	if not sc_change :
		if dict_item[4] != job_dict[key][4]:
			sc_change = True
	if not priority_change :
		if dict_item[5] != job_dict[key][5]:
			priority_change = True
	if not rcpu_change :
		if dict_item[6] != job_dict[key][6]:
			rcpu_change = True
	if not rmem_change :
		if dict_item[7] != job_dict[key][7]:
			rmem_change = True
	if not rdisk_change :
		if dict_item[8] != job_dict[key][8]:
			rdisk_change = True
			
def dump(output_file):
	for item in job_dict:
		write_line = ','.join(job_dict[item])+"\n"
		output_file.write(write_line)
def print_change():
	global sc_change
	global priority_change
	global rcpu_change
	global rmem_change
	global rdisk_change
	sc_can_change = "can be changed" if sc_change else "can not be changed"
	priority_can_change = "can be changed" if priority_change else "can not be changed"
	rcpu_can_change = "can be changed" if rcpu_change else "can not be changed"
	rmem__can_change = "can be changed" if rmem_change else "can not be changed"
	rdisk_can_change = "can be changed" if rdisk_change else "can not be changed"
	print  "scheduling_class "+sc_can_change
	print  "priority "+priority_can_change
	print  "request CPU "+rcpu_can_change
	print  "request MEM "+rmem__can_change
	print  "request Disk "+rdisk_can_change

def main():
	data_files = glob.glob(data_path+csv_files_globbing)
	output_file = open(output_path,'a')
	for one_file in data_files:
		deal(one_file)
	dump(output_file)
	print_change()
	output_file.close()

if __name__ == '__main__':
	main()