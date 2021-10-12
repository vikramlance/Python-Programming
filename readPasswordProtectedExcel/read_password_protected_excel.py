from xlrd import *
import win32com.client
import os


xlApp = win32com.client.Dispatch('Excel.Application')
# read password of excel file from password.txt (warning: this will pick last line in tex file as a passwd)
with open('password.txt') as f:
    for line in f:
        passwd = line

path = os.path.abspath('samplePasswordProtected.xlsx')
xlwb = xlApp.Workbooks.Open(path, False, True, None, passwd)

exclsheet = xlwb.Sheets(1)

lastCol = exclsheet.UsedRange.Columns.Count
print("The last comlumn number is %r" % lastCol)

headers = []
for r in range(1, lastCol + 1):
    headers.append(exclsheet.Cells(1, r).Value)
print(headers)

print('End of file processing.')
