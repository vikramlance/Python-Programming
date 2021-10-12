from xlrd import *
import win32com.client
import csv
import sys

xlApp = win32com.client.Dispatch('Excel.Application')
# print('Excel library version:', xlApp.Version)

xlwb = xlApp.Workbooks.Open(r'samplePasswordProtected.xlsx', False, True, None, 'abc')

print(xlwb)

for i in xlwb:
    print(i)

print('End of file processing.')