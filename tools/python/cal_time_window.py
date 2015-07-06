import csv
import os

base_dir = "F:\\output\\fail_1_ts\\"

def main():
	files = os.listdir(base_dir)
	total = 0.0
	for filename in files:
		total = total +cal(filename)
	average_time_win = total/files.__len__()
	print "average time window is "+str(average_time_win)
def cal(filename):
	with open(base_dir+filename) as csv_file:
		reader = csv.reader(csv_file)
		before_cpu = 1
		max_time_window = 0
		curr_time_window = 0
		end_pos = 0
		for line_list in reader:
			curr_cpu = float(line_list[5])
			if curr_cpu == 0:
				curr_cpu = 0.000001
			diff = curr_cpu/before_cpu
			before_cpu = curr_cpu
			if (diff < 1.3) and (diff > 0.7):
				curr_time_window = curr_time_window + 1
			else:
				if curr_time_window > max_time_window:
					max_time_window = curr_time_window
					end_pos = int(line_list[0])-1
				curr_time_window = 0
		print filename +","+str(max_time_window)+","+str(end_pos-max_time_window) +"," +str(end_pos)
		return max_time_window

if __name__ == '__main__':
	main()