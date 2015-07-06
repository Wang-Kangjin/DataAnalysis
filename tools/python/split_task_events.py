import fileinput
import glob
import csv
import os
import sys

base_path = "F:\\output\\"
data_source = ""
output_path = ""
all_dict={}

def main():
	orignal_files = glob.glob(data_source+"part-*")
	for onefile in orignal_files:
		fill_dict(onefile)
	dump()
def fill_dict(filename):
	print filename
	for line in fileinput.input(filename):
		line_split = line.split('\t')
		key = line_split[0]
		if key not in all_dict:
			all_dict[key] = [line_split[1]]
		else:
			all_dict[key].append(line_split[1])

def dump():
	for key in all_dict:
		wf = open(output_path+'task_event-'+key+'.csv','w')
		lines = []
		write_lines=[]
		for line in all_dict[key]:
			line_list = line.split(',')
			time = line_list[0]
			if time == '0':
				pass
			else:
				time_index = (float(time)- 600000000) / 300000000
				line_list[0] = str(time_index)
				lines.append(line_list)
		lines.sort(lambda x,y:cmp(float(x[0]), float(y[0])))
		for each in lines:
			write_lines.append(','.join(each))
		wf.writelines(write_lines)
		wf.close()



if __name__ == "__main__":
	global data_source
	global output_path
	folder_name = sys.argv[1]
	data_source = base_path+folder_name+"\\"
	output_path = base_path+"task_events_split\\"
	os.mkdir(output_path)
	main()