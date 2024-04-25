"""
Programa_sequencial.py
Descrição: Este programa busca um valor dentro de uma base de dados
Autor: Mateus Chassot Valandro
Data: 19.04.2024
Versão: 0.0.1
"""

# Código de programador

## Alocação de Memória
lista = []
achou = False
posicao = 0
cpf = 0

# Leitura da base de dados do CPF
base = [1,5,2,87,31]
lista = base

# Leitura de dados
cpf = int(input("digite o valor a procurar:"))
# debug com print
print(cpf)

# Processamento de Dados
while posicao < len(lista):
    if lista[posicao] == cpf:
        achou = True
        break
    posicao += 1

# Saída de Dados
if achou: 
    print(f"\nO valor {cpf} foi achado na posição {posicao}.")
else:
    print(f"\no valor {cpf} não foi achado")