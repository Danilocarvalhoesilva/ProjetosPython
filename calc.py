#/usr/bin/env python
# -*- coding: utf-8 -*-

number01 = input("Digite o primeiro número: \n")
number02 = input("Digite o segundo número: \n")
operador = input("Digite uma operação: \n")


result = None

if operador == '+':
    result = float(number01) + float(number02)
elif operador == '-':
    result = float(number01) - float(number02)
else:
    print("Operação inválida!!")
    exit()




print('Resultado da operação é: {0}'.format(result))



"""
for n in number02:
    print(n)
"""