import csv
import os
import fileinput

base_dir = "F:\\output\\diff\\"
fail_time_dir = "F:\\output\\fail_200_failtime\\"
etc_file = "F:\\output\\etc\\train_task.csv"
THRESHOLD=0.1
etc_dict = {}
def main():
	files = os.listdir(base_dir)
	read_etc()
	for filename in files:
		if filename  not in etc_dict:
			continue
		max_freq, max_freq_window = find_max_freq_and_window(filename)
		print filename[9:-4]+','+str(max_freq)+','+str(max_freq_window[1]-max_freq_window[0])

def read_etc():
	with open(etc_file) as csv_etc:
		etc_reader = csv.reader(csv_etc)
		for each in etc_reader:
			train_filename = each[0]
			etc_dict[train_filename] = '1'
def find_max_freq_and_window(filename):
	#print filename[9:-4]
	split_windows = cal(filename)
	for line in fileinput.input(fail_time_dir+filename[9:-4]+".csv"):
		fail_time_list = line.split(",")
		fail_time = int(float(fail_time_list[0]))
		fail_times = int(fail_time_list[1])
		for a_win in split_windows:
			if fail_time>= a_win[0] and fail_time<=a_win[1]:
				if a_win.__len__() == 2:
					a_win.append(1)
				else:
					a_win[2] = a_win[2] + fail_times
				break
			else:
				continue
	max_freq = 0
	max_freq_window=[]
	for each_window in split_windows:
		if each_window.__len__() == 3:
			freq = float(each_window[2])/(each_window[1] - each_window[0])
			if freq>max_freq:
				max_freq = freq
				max_freq_window = [ each_window[0],each_window[1] ]
	return max_freq, max_freq_window

def cal(filename):
	with open(base_dir+filename) as csv_file:
		reader = csv.reader(csv_file)
		before_cpu = 1
		max_time_window = 0
		curr_time_window = 1
		end_pos = 0
		pt = None
		split_windows=[]
		for each in reader:
			pt = each
			if float(each[1]) < THRESHOLD:
				curr_time_window = curr_time_window + 1
			else:
				window = [int(each[0]) - curr_time_window, int(each[0])]
				split_windows.append(window)
				#print str( int(each[0]) - curr_time_window )+":"+each[0]
				curr_time_window = 1
		window = [int(pt[0]) - curr_time_window, int(pt[0])]
		split_windows.append(window)
		return split_windows
		#print str( int(pt[0]) - curr_time_window )+":"+pt[0]
		#print filename +","+str(max_time_window)+","+str(end_pos-max_time_window+1) +"," +str(end_pos)
		#return max_time_window

if __name__ == '__main__':
	main()
	#for each in cal("fail_200-3998246386-0.csv"):
		#print each