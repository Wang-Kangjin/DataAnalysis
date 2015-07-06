import sys

def main():
	job_id = sys.argv[1]
	task_index = sys.argv[2]
	fail_time_file = open("F:\\output\\fail_time\\"+job_id+'_'+task_index+'.txt')
	start_fail_time = int(float(fail_time_file.readline()))
	event_file = open("F:\\output\\output_cpu\\cpu-"+job_id+"-"+task_index+".csv")
	count = 1
	for line in event_file:
		line_split = line.split(',')
		if int(line_split[0]) == start_fail_time:
			print count
			print count+575
			print count+575+24
			return 
		else:
			count = count + 1

if __name__ == '__main__':
	main()