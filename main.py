
nome = input("Digite seu nome: \n")
idade = int(input("Digite sua idade:\n"))
sobrenome = input("Digite seu sobrenome:\n")

print(f"Olá, {nome} {sobrenome}, sua idade é {idade} anos!!")
print(type(idade))
'''
linguagem, nivel, companhia = input().split()

print(linguagem)
print(nivel)
print(companhia)
'''
if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")


