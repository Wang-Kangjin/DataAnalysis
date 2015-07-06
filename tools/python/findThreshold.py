import csv
target_dict={}
base_dir = "F:\output\\fail_1_ts_diff\\fail1-"
def main():
	target_dict["5130456910-0"] = [3000, 4100]
	target_dict["5402488769-555"] = [4100, 6000]
	target_dict["5402488769-2008"] = [3500,4200]
	target_dict["5402488769-2990"] = [1000,2000]
	target_dict["4474140233-14"]   = [1000, 2000]
	target_dict["5921809619-468"] = [3000, 4200]
	target_dict["6114773114-1184"] = [5500, 6200]
	for  key in target_dict:
		print find_max_and_min(key)
def find_max_and_min(key):
	with open(base_dir+key+".csv") as csv_file:
		reader = csv.reader(csv_file)
		max_value = 0
		min_value = 1
		for line_dict in reader:
			time = int(line_dict[0])
			if time > target_dict[key][0] and time < target_dict[key][1]:
				value = float(line_dict[1])
				if value > max_value: 
					max_value = value
				if value < min_value:
					min_value = value
		return (max_value,min_value)
if __name__ == '__main__':
	main()