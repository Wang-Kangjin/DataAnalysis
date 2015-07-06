import fileinput

prefix="F:\\output\\fail_500_split\\"
all_dict={}

def main():
	fill_dict()
	dump()
def fill_dict():
	for line in fileinput.input("F:\\output\\fail_500\\fail_500_combine2"):
		line_split = line.split(',')
		job_id = line_split[2]
		task_id = line_split[3]
		key = 'fail500-' + job_id + '-' + task_id
		if key not in all_dict:
			all_dict[key] = [line]
		else:
			all_dict[key].append(line)

def dump():
	for key in all_dict:
		wf = open(prefix+key+'.csv','w')
		wf.writelines(all_dict[key])
		wf.close()



if __name__ == "__main__":
	main()