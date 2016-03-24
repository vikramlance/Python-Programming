import zipfile
import os

import os.path
import sys
import comtypes.client


if (os.path.isfile("C:/projects/Python-Programming/temp.xml")):
    os.remove("C:/projects/Python-Programming/temp.xml")
    
if (os.path.isfile("C:/word/document.xml")):
    os.remove("C:/word/document.xml")

if (os.path.isfile("C:/projects/Python-Programming/outputFile.docx")):
    os.remove("C:/projects/Python-Programming/outputFile.docx")

f= open("parameter.txt","r")
data=f.read()

data_list=data.split("\n")
newCompany=data_list[0]
newPosition=data_list[1]

print("Reading parameter file")

print("String to find - Tantalus ")

print("String to replace")
print(newCompany)
print("String to find - Sisyphus ")

print("String to replace")
print(newPosition)



replaceText = {"Tantalus" : newCompany, "Sisyphus" : newPosition}
templateDocx = zipfile.ZipFile("C:/projects/Python-Programming/inputFile.docx")
newDocx = zipfile.ZipFile("C:/projects/Python-Programming/outputFile.docx", "a")

with open(templateDocx.extract("word/document.xml", "C:/")) as tempXmlFile:
    tempXmlStr = tempXmlFile.read()

for key in replaceText.keys():
    tempXmlStr = tempXmlStr.replace(str(key), str(replaceText.get(key)))

with open("C:/projects/Python-Programming/temp.xml", "w+") as tempXmlFile:
    tempXmlFile.write(tempXmlStr)

#print(templateDocx.filelist)

for file in templateDocx.filelist:
    if not file.filename == "word/document.xml":
        newDocx.writestr(file.filename, templateDocx.read(file))

newDocx.write("C:/projects/Python-Programming/temp.xml", "word/document.xml")

templateDocx.close()
newDocx.close()

print("new document with replaced strings is available - C:/projects/Python-Programming/outputFile.docx") 

wdFormatPDF = 17

#in_file = os.path.abspath(sys.argv[1])
#out_file = os.path.abspath(sys.argv[2])
in_file = "C:/projects/Python-Programming/outputFile.docx" 
out_file = "C:/projects/Python-Programming/outputFile.pdf" 
word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()
