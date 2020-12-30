from collections import Counter
import openpyxl
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


def write_excell(count):
    book = openpyxl.Workbook()
    sheet = book.active
    sheet['A1'] = 'ID'
    sheet['B1'] = 'Frequency'
    row = 2
    for item in count:
        sheet[row][0].value = item
        sheet[row][1].value = count[item]
        row += 1

    book.save(r'C:\Users\User\Desktop\output.xlsx')
    book.close()


if __name__ == '__main__':
    write_excell(counter(reader(sys.argv[1])))