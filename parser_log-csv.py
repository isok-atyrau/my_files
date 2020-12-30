from collections import Counter
import csv
import sys



def reader(filename):
	
	ips_list = []
	
	with open(filename, 'r') as fl:
		for line in fl:
			ip = line.split('- - ')
			ips_list.append(ip[0])
	
	return ips_list
		
def counter(ips_list):
	
	count = Counter(ips_list)
	
	return count
	
def write_csv(count):
	with open('output.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		
		header = ['IP', 'Frequency']
		writer.writerow(header)
		
		for item in count:
			writer.writerow((item, count[item]))

if __name__ == '__main__':
	write_csv(counter(reader(sys.argv[1])))