# 1. Faça um laço de repetição que comece a contar a partir do número 1 e que vá
# incrementando de 2 em 2 até chegar no número 9. Exemplo de saída que este
# sistema irá gerar quando executá-lo:

i = int(input('Número Inicial: '))
f = int(input('Número Final: '))
p = int(input('Passo: '))
for c in range(i,f+2, p):
     print(c)
     
print("Fim")     
