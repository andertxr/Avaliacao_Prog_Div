# Crie uma API Rest em Python, que responda à seguinte chamada:
# curl -X POST 'http://localhost:5000/soma' -H 'Content-type:
# application/json' -d '{"x": 1, "y": 2}'
# A API /soma irá receber o valor x e somar com o valor y e retorná-lo em JSON no
# seguinte formato:
# {
# "resultado": <valor do resultado>
# }
# Para o exemplo, acima iremos retornar:
# {
# "resultado": 3
# }
# Os valores de entrada, x e y são obrigatórios e devem ser números.
# Tempo estimado: 6-8 minutos. Dificuldade: Fácil.
# 8. Crie um programa que seja uma API de um contador de números. Esta API irá
# manter o número em sua memória, e esta irá iniciar com o valor 0 (zero).
# Para o programa teremos as seguinte chamadas:
# ● POST /contador
# {
# "numero": <numero>
# }
# Irá definir um novo número para o nosso contador. O método irá retornar um
# HTTP 201.
# ● GET /contador
# Retorna o número que foi guardado na memória, em um JSON no formato:
# {
# "numero": <numero guardado>
# }
# E também um HTTP 200.
# ● PUT /contador/incrementa

# Irá incrementar o valor do número em 1 e retornar um HTTP 202.
# ● DELETE /contador
# Irá zerar o valor do contador. A API irá retornar um HTTP 202.

# Exemplo de ter valor em memória com acesso global
CONTADOR = {'contador': 0}

def incrementar():
    CONTADOR['contador'] = CONTADOR['contador']+1

incrementar()

# >>> CONTADOR
# {'contador': 1}

def deletar():
    CONTADOR['contador'] = 0

# >>> CONTADOR
# {'contador': 1}

deletar()

# >>> CONTADOR
# {'contador': 0}