import xlrd
#LER O ARQUIVO
book = xlrd.open_workbook("teste.xlsx")
#PRINTA AS ABAS
#print ("Número de abas: ", book.nsheets)
#PRINTA O NOME DAS PLANILHAS
print ("Nomes das Planilhas:", book.sheet_names())

plan = book.sheets()[0]
#print(plan.get_rows(2))

sh = book.sheet_by_index(0)

#print("TESTE", sh.nrows[1])
#PRINTA NOME DA PLANILHA, LINHAS E COLUNAS
#print(sh.name, sh.nrows, sh.ncols)
#print(sh.row(2))
print("Valor da célula A4 é: ", sh.cell_value(rowx=3, colx=0), "-", sh.cell_value(rowx=3, colx=1))
#for rx in range(sh.nrows):
#    print(sh.row(rx))
