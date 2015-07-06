import csv
import os
import fileinput

base_dir = "F:\\output\\diff\\"
task_usage_dir = "F:\\output\\fail_200_split_ts\\"
fail_time_dir = "F:\\output\\fail_500_failtime\\"
THRESHOLD=0.1

def main():
	files = os.listdir(base_dir)
	for filename in files:
		max_freq, max_freq_window = find_max_freq_and_window(filename)
		print filename[9:-4]+','+str(max_freq)+','+str(max_freq_window[1]-max_freq_window[0])
def find_max_freq_and_window(filename):
	#print filename[9:-4]
	split_windows = cal(filename)
	for line in fileinput.input(fail_time_dir+filename[9:-4]+".txt"):
		fail_time = int(float(line))
		for a_win in split_windows:
			if fail_time>= a_win[0] and fail_time<=a_win[1]:
				if a_win.__len__() == 2:
					a_win.append(1)
				else:
					a_win[2] = a_win[2] + 1
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
		found_first_seg = False
		pt = None
		split_windows=[]
		first_window_avg=0
		origin_usage = []
		counter_for_usage = 0
		for usage_list in csv.reader( open(task_usage_dir+filename )):
			origin_usage.append( float(usage_list[5]) )
		for each in reader:
			pt = each
			if not found_first_seg:
				if float(each[1]) < THRESHOLD:
					curr_time_window = curr_time_window + 1
					counter_for_usage = counter_for_usage + 1
					
				else:
					first_window_avg = average(origin_usage[0:curr_time_window])
					found_first_seg = True
					window = [int(each[0]) - curr_time_window, int(each[0])]
					split_windows.append(window)
					counter_for_usage = counter_for_usage + 1
					curr_time_window = 1
			else:
				if float(each[1]) < THRESHOLD:
					curr_time_window = curr_time_window + 1
					counter_for_usage = counter_for_usage + 1
				else:
					curr_window_avg = average(origin_usage[int(each[0]) - curr_time_window: int(each[0])])
					if abs(origin_usage[counter_for_usage] - first_window_avg) < abs(origin_usage[counter_for_usage] - curr_window_avg):
						curr_time_window = curr_time_window + 1
						counter_for_usage = counter_for_usage + 1
					else:
						window = [int(each[0]) - curr_time_window, int(each[0])]
						split_windows.append(window)
						#print str( int(each[0]) - curr_time_window )+":"+each[0]
						curr_time_window = 1
						counter_for_usage = counter_for_usage + 1
		if (int(pt[0]) - curr_time_window+1) != int(pt[0]):
			window = [int(pt[0]) - curr_time_window+1, int(pt[0])]
			split_windows.append(window)

		return split_windows
		#print str( int(pt[0]) - curr_time_window )+":"+pt[0]
		#print filename +","+str(max_time_window)+","+str(end_pos-max_time_window+1) +"," +str(end_pos)
		#return max_time_window

def average(list_param):
	if list_param.__len__() == 0:
		return 0.0
	total = 0.0
	for each in list_param:
		total = total + each
	return total/list_param.__len__()

if __name__ == '__main__':
	main()
	#for each in cal("fail_200-5389889218-8.csv"):
		#print each