# !/usr/bin/python
# -*- coding: UTF-8 -*-
import csv,os
exampleFile = open('D:\\dmplay\\test\\payTime.csv')
exampleReader = csv.reader(exampleFile)
#exampleData = list(exampleReader)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

os.chdir('D:\\dmplay\\test')
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputFile.close()