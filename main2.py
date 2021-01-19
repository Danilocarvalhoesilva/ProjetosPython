# -*- coding: iso-8859-1 -*-
import sys
import pandas
import requests
from io import BytesIO
#from requests_ntlm import HttpNtlmAuth

chrExecute = sys.argv[1]
strEquipe = sys.argv[2]
fileName = sys.argv[3]

if chrExecute == 'N':
    sys.exit(0)

username = 'srvsla@boticario.net'
password = 'M0n1t0r1@2010'
#r = requests.get("http://tipp.boticario.net/ti/infra/Documentos%20Compartilhados/Escala_Sobre_Aviso_-_TI_Infraestrutura.xlsx",auth=HttpNtlmAuth(username,password))
#r = "Escala_Sobre_Aviso.xlsx"


url = 'https://github.com/Dragonyk/leitura-plantonistas/raw/main/Escala_Sobre_Aviso_-_TI_Infraestrutura.xlsx'
r = requests.get(url)
worksheet = pandas.read_excel(BytesIO(r.content), sheet_name='Plantonistas')

num_rows = len(worksheet)
num_cols = len(worksheet.columns)

result_data = []
for curr_row in range(0, num_rows, 1):
    row_data = []
    for curr_col in range(0, num_cols, 1):
        data = worksheet.iloc[curr_row][curr_col]
        # print(data)
        row_data.append(data)
    result_data.append(row_data)
for line in result_data:
    if strEquipe in line[0]:
        nomePlantonista = str(line[1])
        # if strEquipe.find("Horario ADM") < 0 or strEquipe.find("Sem Plantao") < 0:
        if line[1]:
            if line[3]:
                line[3] = line[3].replace('(', '')
                line[3] = line[3].replace(')', '')
                line[3] = line[3].replace('-', '')
                line[3] = line[3].replace(' ', '')
                line[3] = line[3].replace('|', '')
                contatoPlantonista = ('55' + str(line[3]))
            if line[7]:
                line[7] = line[7].replace('(', '')
                line[7] = line[7].replace(')', '')
                line[7] = line[7].replace('-', '')
                line[7] = line[7].replace(' ', '')
                line[7] = line[7].replace('|', '')
                contatoEscalation1 = ('55' + str(line[7]))
            if line[7]:
                line[9] = line[9].replace('(', '')
                line[9] = line[9].replace(')', '')
                line[9] = line[9].replace('-', '')
                line[9] = line[9].replace(' ', '')
                line[9] = line[9].replace('|', '')
                contatoEscalation2 = ('55' + str(line[9]))

print('')
print('Grupo Resolvedor: ' + str(strEquipe))
#print('Nome Plantonista: ' + str(nomePlantonista))
#print('Contato Plantonista: ' + str(contatoPlantonista))
print('Contato Escalation 1: ' + str(contatoEscalation1))
print('Contato Escalation 2: ' + str(contatoEscalation2))
