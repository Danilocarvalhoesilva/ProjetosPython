import xlrd

wb = xlrd.open_workbook('teste.xlsx', on_demand = True)#file_contents=r.content, on_demand = True)
sh = wb.sheet_by_index(0)  


data = []
ncol= sh.ncols -4
for col in range(ncol):
    data.append( sh.cell_value(2,col) )

newdata = []
for row in range(1, sh.nrows):
    elm = {}
    for col in range(ncol):
        elm[data[col]]=sh.cell_value(row,col)
    newdata.append(elm)
print("RESULTADO")
newdata=newdata[4].items()

for x,y in newdata:
    print(x,y)
#print(sh.row(3))
#lookup = dict(zip(sh.col_values(0, 3, 23), sh.col_values(0, 0, 0)))
#print(lookup)
