import os
import csv

def startWith(*startstring):
        starts = startstring
        def run(s):
                f = map(s.startswith,starts)
                if True in f: return s
        return run

def read_file(filename):
	global path
	global jobs
	global tasks
	f = open(path + filename, "r")
	lines = f.readlines()
	for line in lines:
		words = line.replace('(', '').replace(')', '').split(',')
		for i in xrange(0,len(jobs)):
			if words[0] == jobs[i] and words[1] == tasks[i]:
				start = (float(words[2]) - 600000000) / 300000000
				end = (float(words[3]) - 600000000) / 300000000
				fws[i].writelines(words[0] + "\t" + words[1] + "\t" + str(start) + "\t" + str(end) + "\t" + words[4])
				break
	f.close()

path = "f:\\output\\cpu\\"
jobs = ["5285926325","6274166915","6111537791","6353820544","6130716573","6130716573","3536441868","4297552690","6126024662","4297551713","6157428805","5349360858","6316376215",\
"6316376295","6316376261","6316376180","6212822642","6404623218","6291099581","6352644496","6323287875","6338507766"]
tasks = ["0","0","0","0", "0","0","0","0","0","0","2","2","0","0","0","0","0","218","566","13","66","884"]
fws = []
for i in xrange(0,len(jobs)):
	fws.append(open("f:\\task\\cpuls\\" + jobs[i] + "_" + tasks[i] + ".txt", "w"))
listfile = os.listdir(path)
a = startWith("part-")
listfile = filter(a, listfile)
for filename in listfile:
	read_file(filename)
for i in xrange(0,len(jobs)):
	fws[i].close()
# read_csv("part-00000-of-00500.csv")
# print len(jobs)
