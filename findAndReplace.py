#!/usr/bin/env python3
import fileinput
import sys, getopt

#import win32com.client
from docx import Document

'''for arg in sys.argv:
    print(arg)
'''    

'''f= open("parameter.txt","r")
data=f.read()

data_list=data.split("\n")
newCompany=data_list[0]
newPosition=data_list[1]

f = open("inputFile.docx","r")
filedata = f.read()
f.close()

newdata = filedata.replace("company",newCompany)
newdata1 = newdata.replace("position1",newPosition)

f = open("outputFile.docx","w")
f.write(newdata1)
f.close() '''

f= open("parameter.txt","r")
data=f.read()

data_list=data.split("\n")
newCompany=data_list[0]
newPosition=data_list[1]

MSWord.Documents.Open("inputFile.docx")
Selection = MSWord.Selection

find = Selection.Find
find.Text = "Tantalus"
find.Replacement.Text = newCompany

find.Text = "Sisyphus"
find.Replacement.Text = newPosition

document.save('inputFile.docx')
MSWord.Documents.Close("inputFile.docx")
MSWord.Quit

