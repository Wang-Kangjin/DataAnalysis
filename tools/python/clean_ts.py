import fileinput
import os
import csv
import sys

data_path="F:\\output\\fail_1_split\\"
output_path="F:\\output\\fail_1_ts\\"

def main():
	files = os.listdir(data_path)
	for one_file in files:
		do(one_file)

def do(filename):
	time_dict = {}
	print data_path+filename
	with open(data_path+filename) as csvfile:
		reader = csv.reader(csvfile)
		for line_list in reader:
			start_time = long(line_list[0])
			time_index = (start_time - 600000000) / 300000000
			if time_index not in time_dict:
				time_dict[time_index] = [line_list]
			else:
				time_dict[time_index].append(line_list)
	output_buffer = []
	for one_interval in sorted(time_dict.keys()):
		usage_list = time_dict[one_interval]
		count_in_interval = usage_list.__len__()
		job_id = usage_list[0][2]
		task_id = usage_list[0][3]
		machine_id = usage_list[0][4]
		start_time = str(one_interval)
		end_time   = str(one_interval+1)
		final_list=[start_time,end_time,job_id,task_id,machine_id]
		for x in range(5,20):
			attr = float(0)
			for y in range(count_in_interval):
				if usage_list[y][x] == '':
					usage_list[y][x] = 0
				attr = float(usage_list[y][x]) + attr
			final_list.append( str(attr/count_in_interval) )
		line = ','.join(final_list)+"\n"
		output_buffer.append(line)
	output_file = open(output_path+filename,"a")
	output_file.writelines(output_buffer)
	output_file.close()



if __name__ == "__main__":
	global data_path
	global output_path
	folder_name = sys.argv[1]
	data_path = "F:\\output\\"+ folder_name+"\\"
	output_path="F:\\output\\"+ folder_name +"_ts\\"
	os.mkdir(output_path)
	main()