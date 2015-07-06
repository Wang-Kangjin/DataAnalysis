import fileinput
import os

data_path="/home/kangjin/output_cpu/"

def main():
	files = os.listdir(data_path)
	for one_file in files:
		do(one_file)

def do(filename):
	all_zero = True
	#print data_path+filename
	fp = fileinput.input(data_path+filename)
	for line in fp:
		line_split = line.split(",")
		cpu_usage = float(line_split[2][:-1])
		if cpu_usage != 0:
			all_zero = False
			break
	if all_zero :
		print filename +" is all zero"
	fp.close()



if __name__ == "__main__":
	main()