import bs4
import requests
import lxml
import xlwt
import time
import re

from urls import link1

def chunkstring(string, length):
    return re.findall('.{%d}' % length, string)

book = xlwt.Workbook()        # make the excel file
j = 0
for each in link1:
    j = j + 1
    print(j)
    sheet = book.add_sheet(str(j))       # add the sheet name
    html = requests.get(each)
    text = html.text
    n = 30000
    result = chunkstring(text, n)
    
    sheet.write(0,0,'HTML')
    k = 0
    for part in result:
        k = k + 1
        sheet.write(k,0, part)
    
book.save("test1.xls")