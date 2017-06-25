#!usr/bin/python

# @author ziyaj

COURSE = 'CPSC304'

def check(course):
    course = course.upper()
    file = open('output/report.txt', 'r')
    for line in file:
        if course in line:
            formatPrint(line)
    file.close()

def formatPrint(line):
    index = line.find(',')
    course = line[:index]
    index += 1
    line = line[index:]
    index = line.find(',')
    section = line[:index]
    index += 1
    line = line[index:]
    index = line.find(',')
    instructor = line[:index]
    index += 1
    line = line[index:]
    index = line.find(',')
    remaining = line[:index]
    index += 1
    line = line[index:]
    index = line.find(',')
    registered = line[:index]
    index += 1
    line = line[index:]
    total = line

    print(course + ' ' + section + ' - ' + instructor)
    print('remaining: ' + remaining)
    print('registered: ' + registered)
    print('total: ' + total)

def main():
    check(COURSE)

main()