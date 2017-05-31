# !/usr/bin/python
# -*- coding: UTF-8 -*-
# http://openpyxl.readthedocs.io/en/default/usage.html
import openpyxl
wb = openpyxl.load_workbook('D:\\dmplay\\test\\payTime.xlsx')
wb.get_sheet_names()
#sheet = wb.get_sheet_by_name('Sheet3')
sheet = wb.get_active_sheet()
print(sheet.title)
for i in range(1, 8, 2):
    print(i, sheet.cell(row=i, column=2).value)

for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
        print('--- END OF ROW ---')


for cell in sheet.rows:
    for cellObj in cell:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')

for cell in sheet.columns:
    for cellObj in cell:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF columns ---')