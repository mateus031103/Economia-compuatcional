"""
Programa_sequencial.py
Descrição: Este programa busca um valor dentro de uma base de dados
Autor: Mateus Chassot Valandro
Data: 19.04.2024
Versão: 0.0.3 
Correções realizadas: 
1 - informação mais intuitiva para o usuário da posição do número
2 - informação mais precisa de o valor procurado é um cpf
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
cpf = int(input("digite o CFP a procurar:"))
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
    print(f"\nO CPF {cpf} foi achado na posição {posicao + 1}.")
else:
    print(f"\nO CPF {cpf} não foi achado")