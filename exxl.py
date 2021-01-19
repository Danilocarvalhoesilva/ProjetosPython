import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import sys
import requests
import urllib.request
from collections import defaultdict

i = int(sys.argv[1])

if i > 23:
    print ('''
    DIGITE O NUMERO DE ACORDO COM A EQUIPE:
    0 - TI - INFRA - Monitoramento
    1 - TI - INFRA - Backup
    2 - TI - INFRA - Datacenter Operations
    3 - TI - INFRA - AS 400
    4 - TI - INFRA - WEB
    5 - TI - INFRA - Banco de Dados
    6 - TI - INFRA - Basis
    7 - TI - INFRA - GAC
    8 - TI - INFRA - Segurança
    9 - Gestao de Crise
    10 - TI - INFRA - Central Telefonica
    11 - TI - INFRA - Rede Fisica
    12 - TI - SERVIÇOS - EndPoints Acessos
    13 - Segurança WAF
    14 - TI - SERVIÇOS - Sustentaçao Varejo VD
    15 - TI - SERVIÇOS - Sustentaçao Varejo Lojas
    16 - TI - SERVIÇOS - Sustentaçao Colabore
    17 - TI - SERVIÇOS - SUSTENTAÇAO BI
    18 - Command Center
    19 - TI - INFRA - Job Scheduling
    ''')
    sys.exit(0)

#username = 'srvsla@boticario.net'
#password = 'M0n1t0r1@2010'
#read = requests.get("http://tipp.boticario.net/ti/infra/Documentos%20Compartilhados/Escala_Sobre_Aviso_-_TI_Infraestrutura.xlsx",auth=HttpNtlmAuth(username,password))

##BAIXANDO A PLANILHA
url = 'https://github.com/Dragonyk/leitura-plantonistas/raw/main/Escala_Sobre_Aviso_-_TI_Infraestrutura.xlsx'
r = requests.get(url, allow_redirects=True)

rb = open_workbook(file_contents=r.content, on_demand = True)                    
wb = copy(rb)

s = wb.get_sheet(0)                                 
s.write(3,0,'TI - INFRA - Monitoramento')           
wb.save(rb)

open('teste.xlsx', 'wb').write(r.content)

###ABRE O ARQUIVO
workbook = xlrd.open_workbook('teste.xlsx', on_demand = True)#file_contents=r.content, on_demand = True)
ws = workbook.sheet_by_index(0)

first_row = [] 
ncol = ws.ncols -4
for col in range(ncol):
    first_row.append( ws.cell_value(2,col) )

# CRIANDO UM DICIONARIO
data =[]
t="-"
for row in range(3, ws.nrows):
    elm = {}
    for col in range(ncol):
        elm[first_row[col]]=ws.cell_value(row,col)
    data.append(elm)
    

print('RESULTADO:')
data = data[i].items() 
for x,y in data:
    print(x,y)
#print(data[i])
