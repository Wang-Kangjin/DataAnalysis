import csv

def main():
	deal_file()

def deal_file(filename):
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		for x in xrange(0,reader.__len__()):
			for y in xrange(x,reader.__len__())
				varr(x,y,reader)

if __name__ == '__main__':
	main()