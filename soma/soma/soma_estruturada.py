"""
Programa Soma Estruturada
Descrição: Este programa faz a soma de duas parcelas digitadas pelo usuário
Autor: mateus chassot valandro
Data: 03.05.2024
Versão: 0.0.1
"""
# Definição de variáveis
i = 0
numeros = [0,0]
soma = 0

# Entrada de Dados
while i < 2:
    numeros[i] = int(input(f'digite a parcela {i+1}:'))
    i += 1

# Processamento de dados
soma = numeros[0] + numeros[1]

# Saída de Dados
print( f' A soma do número {numeros[0]} e do numero {numeros[1]} é {soma}')