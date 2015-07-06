import fileinput

prefix="/home/kangjin/output/fail_500_split/fail500-"
def main():
	current_interval = 0
	for line in fileinput.input("/home/kangjin/output/fail_500/fail500_combine"):
		line_split = line.split(',')
		job_id = line_split[2]
		task_id = line_split[3]
		output_file = open(prefix+job_id+"-"+task_id+".csv","a")
		output_file.write(line)
		output_file.close()


if __name__ =="__main__":
	main()