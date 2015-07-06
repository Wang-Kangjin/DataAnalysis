import csv 
import os
base_dir = "F:\\output\\test\\"
base_output_dir = "F:\\output\\test\\"
def main():
	file_list = os.listdir("F:\\output\\test\\")
	for filename in file_list:
		cal_file(filename)
	#cal_file("F:\\output\\fail_1_ts\\fail1-5402488769-743.csv")

def cal_file(filename):
	print filename
	with open(base_dir+filename) as csv_file:
		csv_reader = csv.reader(csv_file)
		before_cpu = 1
		result=[]
		for line_list in csv_reader:
			curr_cpu = float(line_list[5])
			if curr_cpu == 0:
				curr_cpu = 0.000001
			diff = curr_cpu/before_cpu
			before_cpu = curr_cpu
			res_line = str(line_list[0])+','+str(diff)#+'\n'
			print res_line
			result.append(res_line)
		##fw = open(base_output_dir+filename,"a")
		#fw.writelines(result)
		#fw.close()

if __name__ == '__main__':
	main()