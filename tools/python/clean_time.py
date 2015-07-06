import fileinput
import os

data_path="/home/kangjin/output/"
output_path="/home/kangjin/output_cpu/"

def main():
	files = os.listdir(data_path)
	for one_file in files:
		do(one_file)

def do(filename):
	time_dict = {}
	print data_path+filename
	for line in fileinput.input(data_path+filename):
		line_split = line.split(",")
		start_time = long(line_split[2])
		time_interval_index = (start_time - 600000000) / 300000000
		cpu_usage = float(line_split[4])
		if time_interval_index not in time_dict:
			time_dict[time_interval_index] = [cpu_usage]
			count_in_one_interval = 0
		else:
			if cpu_usage == 0 :
				continue
			else:
				time_dict[time_interval_index].append(cpu_usage)
	for one_interval in sorted(time_dict.keys()):
		usage_list = time_dict[one_interval]
		average = sum(usage_list) / usage_list.__len__()
		output_file = open(output_path+filename,"a")
		start_time = one_interval
		end_time = one_interval+1
		line = str(start_time) + ","+ str(end_time)+ "," + str(average)+"\n"
		output_file.write(line)



if __name__ == "__main__":
	main()