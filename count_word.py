from collections import Counter
import sys

counter = Counter()

def main(filename):
	with open(filename, 'r', encoding='utf-8') as fl:
		for line in fl.readlines():
			words = line.split()
			for word in words:
				filtered_word = word.strip('.').strip(',').strip('"').strip('!').strip('?').strip('(').strip('-').lower()
				if filtered_word:
					counter[filtered_word] += 1
	return counter


if __name__ == '__main__':
	counter = main(sys.argv[1])
	for key, value in counter.most_common(10):
		print(f'{key} ----- {value}')
				









