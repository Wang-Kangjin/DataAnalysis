import fileinput
import glob
import csv

data_source = "F:\\output\\fail_1_top2900\\"
#data_source = "F:\\output\\test\\"
fail_1_prefix="F:\\output\\fail_1_split_additioin\\fail_1-"
fail_4000_prefix = "F:\\output\\fail_4000_split\\fail_4000-"
fail_top3000_prefix = "F:\\output\\fail_200_split\\fail_200-"
etc_file = "F:\\output\etc\\fail_top3000.csv"
all_dict={}
etc_dict={}

def main():
	orignal_files = glob.glob(data_source+"part-*")
	read_etc()
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
		if key not in etc_dict:
			continue
		if key not in all_dict:
			all_dict[key] = [line]
		else:
			all_dict[key].append(line)
def read_etc():
	with open(etc_file) as csv_file:
		csv_reader = csv.reader(csv_file)
		count = 0
		for line in csv_reader:
			count = count + 1
			if line[0].startswith('#'):
				continue
			key = line[0]+'-'+line[1]
			fail_time = 0
			if count < 1890:
				fail_time = line[2]
			else:
				fail_time = 1
			etc_dict[key] = fail_time

def dump():
	for key in all_dict:
		print key+'->'+etc_dict[key]
		if int(etc_dict[key]) > 4000:
			wf = open(fail_4000_prefix+key+'.csv','w')
			wf.writelines(all_dict[key])
			wf.close()
			continue
		if int(etc_dict[key]) > 200:
			print ">200"+fail_top3000_prefix
			wf = open(fail_top3000_prefix+key+'.csv','w')
			wf.writelines(all_dict[key])
			wf.close()
			continue
		wf = open(fail_1_prefix+key+'.csv','w')
		wf.writelines(all_dict[key])
		wf.close()



if __name__ == "__main__":
	main()