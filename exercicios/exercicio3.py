#3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Qual o sexo?\n ")

if sexo == 'F' or sexo == 'f':
    print("F - Feminino")
if sexo == 'M' or sexo == 'm':
    print("M - Masculino")
else:
    print("Sexo Indefinido")
