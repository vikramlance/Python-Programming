"""
This program will run on windows, might not work on other OS.
"""

import os
import win32com.client


xlApp = win32com.client.Dispatch('Excel.Application')
# read password of excel file from password.txt (warning: this will pick last line in text file as a passwd)
with open('password.txt') as f:
    for line in f:
        passwd = line

path = os.path.abspath('samplePasswordProtected.xlsx')
xlwb = xlApp.Workbooks.Open(path, False, True, None, passwd)

output_path = os.path.abspath('samplePasswordProtected2.xlsx')
xlwb.SaveAs(output_path, None, '', '')

xlApp.Quit()

print('End of file processing.')
