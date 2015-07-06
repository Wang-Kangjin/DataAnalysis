import os
import csv

def startWith(*startstring):
        starts = startstring
        def run(s):
                f = map(s.startswith,starts)
                if True in f: return s
        return run

path = "fail_500_evicttime_spark\\"
listfile = os.listdir(path)
a = startWith("part-")
listfile = filter(a, listfile)
for filename in listfile:
	f = open(path + filename, "r")
	lines = f.readlines()
	for line in lines:
		words = line.replace('(', '').replace(')', '').split(',')
		job = words[0]
		task = words[1]
		print words
		fw = open("f:\\task\\fail_500_evicttime\\" + job + "-" + task + ".txt", "a")
		fw.writelines(words[2])
		fw.close()

