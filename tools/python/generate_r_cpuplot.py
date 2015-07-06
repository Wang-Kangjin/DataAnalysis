import os
import csv


def readAndWrite(filename):
	global path
	global fw
	global path2
	task = filename[8:len(filename)-4]
	fw.writelines("cpu<-read.csv(\"" + path + filename + "\",header=F)\n")
	fw.writelines("fail_point<-read.table(\"" + path2 + task + ".txt\",header=F)\n")
	fw.writelines("evict_point<-read.table(\"" + path3 + task + ".txt\",header=F)\n")
	fw.writelines("kill_point<-read.table(\"" + path4 + task + ".txt\",header=F)\n")
	fw.writelines("cpu.ts<-ts(cpu[,6],start=cpu[1,1],freq=1)\n")
	fw.writelines("png(file=\"" + "tsplot_fail_500_2\\\\" + task + ".png\",width=1280,height=720)\n")
	fw.writelines("plot(cpu.ts)\n")
	fw.writelines("points(fail_point[,1],fail_point[,2],col=2, pch=0)\n")
	fw.writelines("points(evict_point[,1],evict_point[,2],col=\"blue\", pch=1)\n")
	fw.writelines("points(kill_point[,1],kill_point[,2],col=\"green\", pch=2)\n")
	fw.writelines("legend(\'topright\',c(\"fail point\",\"evict point\",\"kill point\"),col=c(2,\"blue\",\"green\"), pch=c(0,1,2))\n")
	fw.writelines("dev.off()\n")
	fw.writelines("rm(list=c(\"fail_point\",\"evict_point\",\"kill_point\"))\n")

path = "f:\\\\task\\\\fail_500_ts\\\\"
path2 = "f:\\\\task\\\\fail_500_failpoints\\\\"
path3 = "f:\\\\task\\\\fail_500_evictpoints\\\\"
path4 = "f:\\\\task\\\\fail_500_killpoints\\\\"
listfile = os.listdir(path)
fw = open("fail_500_cpu_plot_2.r", "w")
for filename in listfile:
	readAndWrite(filename)
fw.close()