import csv
import os

base_dir = "fail_500_ts\\"
base_dir2 = "fail_500_failnum\\"

fw_pred = open("predict_result_leadtime.txt", "w")
window_length = 1
freq = 1
def main():
	files = os.listdir(base_dir)
	# print predict(base_dir + "fail500-5656479838-0.csv", base_dir2 + "5656479838-0.csv")
	for filename in files:
		words = filename[8:len(filename)].split("-")
		job = words[0]
		task = words[1]
		label = predict(base_dir + filename, base_dir2 + job + "-" + task)
		if label != None:
			fw_pred.writelines(job + " " + task + " 1 " + str(label) + "\n")
		else:
			fw_pred.writelines(job + " " + task + " " + str(label) + "\n")
	fw_pred.close()

def predict(tsfile, failfile):
	with open(tsfile) as csv_file:
		reader = csv.reader(csv_file)
		before_cpu = 1
		diffs = []
		count = 0
		for line_list in reader:
			curr_cpu = float(line_list[5])
			# print line_list
			count = count + 1
			if before_cpu != 1:
				diff = abs(curr_cpu - before_cpu)
				# print diff
				diffs.append(diff)
			before_cpu = curr_cpu
		max_diff = max(diffs)
		min_diff = min(diffs)
	if max_diff == 0:
		return
	fail_times = {}
	with open(failfile) as fail_file:
		reader = csv.reader(fail_file)
		for line in reader:
			fail_times[line[0]] = line[1]
	with open(tsfile) as csv_file2:
		fail_num = 0
		before_pos = 0
		before_cpu = 1
		reader2 = csv.reader(csv_file2)
		count2 = 0

		for line_list in reader2:
			curr_cpu = float(line_list[5])
			count2 = count2 + 1
			if before_cpu != 1:
				diff = abs(curr_cpu - before_cpu)/(max_diff - min_diff)
				fail_freq = float(fail_num)/(int(line_list[0])- int(before_pos))
				if fail_freq > freq:
					return int(line_list[0]) - 1
				if diff > 0.1:
					# print line_list
					after_pos = int(line_list[0])
					before_pos = line_list[0]
					fail_num = 0
				# elif count2 == count:
				# 	after_pos = int(line_list[0])
				# 	if line_list[0] in fail_times.keys():
				# 		fail_num = fail_num + int(fail_times[line_list[0]])
			else:
				before_pos = line_list[0]
			before_cpu = curr_cpu
			if line_list[0] in fail_times.keys():
				fail_num = fail_num + int(fail_times[line_list[0]])

if __name__ == '__main__':
	main()