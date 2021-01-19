import xlrd
 
loc = ("teste.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
sheet.cell_value(0, 0)
for rownum in range(sheet.nrows):

    print(sheet.row_values(rownum))
 
