import os
import random
import sys
data_dir = "F:\\output\\fail_200_ts\\"
def main():
	file_list = os.listdir(data_dir)
	left_file_number = int( file_list.__len__() * 0.7)
	while left_file_number >0:
		file_index = random.randint(0,file_list.__len__()-1)
		if sys.argv[1] == 'train':
			print file_list[file_index]
		file_list.remove(file_list[file_index])
		left_file_number = left_file_number -1
	if sys.argv[1] == "test":
		for filename in file_list:
			print filename

if __name__ == '__main__':
	main()