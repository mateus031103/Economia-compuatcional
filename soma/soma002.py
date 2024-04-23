"""
Programa Soma
Descrição: este programa faz a soma de dois números inteiros digitados pelo usuário e exibe o seu resultado na tela.
Autor: Mateus Chassot Valandro
# Data 13/04/2024
Versão: 0.0.2
"""
# Alocação de Memória
i: i = 0
numero: int = 0
soma: int = 0

# Entrada de Dados e Processamento de Dados
while i <2:
    numero = int(input(f"Digite a parcela {i+1}:"))
    soma = soma + numero
    i+=1

# Saída de Dados
print(f"A soma dos números é igual a {soma}")



