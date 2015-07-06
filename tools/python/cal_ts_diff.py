import csv 
import os
base_dir = "F:\\output\\fail_200_next_3k_split_ts\\"
base_output_dir = "F:\\output\\diff\\"
def main():
	file_list = os.listdir(base_dir)
	for filename in file_list:
		cal_file(filename)
	#cal_file("F:\\output\\fail_1_ts\\fail1-5402488769-743.csv")

def cal_file(filename):
	print filename
	with open(base_dir+filename) as csv_file:
		csv_reader = csv.reader(csv_file)
		before_cpu = 1
		wls=[]
		normaled_list = normalization(csv_reader)
		for each in normaled_list:
			wl =  each[0]+','+each[5]+'\n'
			wls.append(wl)
		fw = open(base_output_dir+filename,'w')
		fw.writelines(wls)
		fw.close()

def normalization(reader):
	diff_max = 0.0
	diff_min = float("inf")
	origin_list=[]
	before_cpu = float(reader.next()[5])
	count = 0
	for each_list in reader:
		curr_cpu = float(each_list[5])
		curr_diff = 0
		if count == 0:
			each_list[5] = 0.0
			origin_list.append(each_list)
		else:
			curr_diff = abs(curr_cpu - before_cpu)
			if curr_diff > diff_max:
				diff_max = curr_diff
			elif curr_diff < diff_min:
				diff_min = curr_diff
			each_list[5] = curr_diff
			origin_list.append(each_list)
		before_cpu = curr_cpu
		count = count + 1
	for each_list in origin_list:
		each_list[5] = str( each_list[5]/(diff_max - diff_min) )
	return origin_list

if __name__ == '__main__':
	main()