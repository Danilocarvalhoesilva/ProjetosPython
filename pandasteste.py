import xlwings as xw
import pandas as pd

#create DF
months = ['2017-01','2017-02','2017-03','2017-04','2017-05','2017-06','2017-07','2017-08','2017-09','2017-10','2017-11','2017-12']
value1 = [x * 5+5 for x in range(len(months))]
df = pd.DataFrame(value1, index = months, columns = ['value1'])
df['value2'] = df['value1']+5
df['value3'] = df['value2']+5

#load workbook that has a chart in it
wb = xw.Book('teste.xlsx')

ws = wb.sheets['chartData']

ws.range('A1').options(index=False).value = df

wb = xw.Book('teste.xlsx')

xw.apps[0].quit()


'''
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("teste.xlsx")
wb = copy(rb)

s = wb.get_sheet(0)
s.write(3,0,'TI - INFRA - Monitoramento')
wb.save('teste.xlsx')
'''
