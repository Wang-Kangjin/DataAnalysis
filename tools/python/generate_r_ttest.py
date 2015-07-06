import os
import csv


def readAndWrite(filename):
	global path
	global fw
	global path2
	task = filename[0:len(filename)-4]
	fw.writelines("run_point<-read.table(\"" + path + filename + "\",header=F)\n")
	fw.writelines("fail_point<-read.table(\"" + path2 + task + ".txt\",header=F)\n")
	fw.writelines("sink(\"ttest_mem_fail_500\\\\"+ task + ".txt\")\n")
	fw.writelines("t.test(run_point[,3],fail_point[,3])\n")
	fw.writelines("sink()\n")
	fw.writelines("rm(list=c(\"fail_point\",\"run_point\"))\n")

path = "f:\\\\task\\\\fail_500_runpoints\\\\"
path2 = "f:\\\\task\\\\fail_500_failpoints\\\\"
listfile = os.listdir(path2)
fw = open("fail_500_ttest_mem.r", "w")
for filename in listfile:
	readAndWrite(filename)
fw.close()