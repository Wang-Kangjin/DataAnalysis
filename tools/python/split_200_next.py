import fileinput
import glob
import csv

data_source = "F:\\output\\fail_200_next_3k\\"
#data_source = "F:\\output\\test\\"
output_prefix = "F:\\output\\fail_200_next_3k_split\\fail_200-"
all_dict={}

def main():
	orignal_files = glob.glob(data_source+"part-*")
	for onefile in orignal_files:
		fill_dict(onefile)
	dump()
def fill_dict(filename):
	print filename
	for line in fileinput.input(filename):
		line_split = line.split(',')
		job_id = line_split[2]
		task_id = line_split[3]
		key = job_id + '-' + task_id
		if key not in all_dict:
			all_dict[key] = [line]
		else:
			all_dict[key].append(line)

def dump():
	for key in all_dict:
		wf = open(output_prefix+key+'.csv','w')
		wf.writelines(all_dict[key])
		wf.close()



if __name__ == "__main__":
	main()