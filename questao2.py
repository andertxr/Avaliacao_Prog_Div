# 2. Elabore um programa que leia um número que o usuário digitar.
# Dependendo do número informado, das frases abaixo,
# o sistema imprimirá somente as que forem verdadeiras.

num = int(input('Por Gentileza, Escolha e Insira um Número: '))
resto = num % 2

if num < 10:
    print("O numero escolhido é menor do que 10.")

if resto == 0:
    print("O número escolhido é par.") 

if num >= 8 and num <= 16:
    print("O número escolhido está entre 8 e 16.")

if num == 51 or num == 80:
    print("O número escolhido é 51 ou 80.")
    
print("Fim")    