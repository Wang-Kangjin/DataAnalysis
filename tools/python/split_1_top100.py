import fileinput

prefix="F:\\output\\fail_1_split\\fail1-"
all_dict={}

def main():
	fill_dict()
	dump()
def fill_dict():
	for line in fileinput.input("F:\\output\\fail_1_top100\\fail_1_top100_combine.csv"):
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
		print key
		wf = open(prefix+key+'.csv','w')
		wf.writelines(all_dict[key])
		wf.close()



if __name__ == "__main__":
	main()