"""
Programa Procedural
Descrição:
Autor: mateus Chassot valadro
Data:03.05.2024
versão: 0.0.1
"""
# Definição da função de entrada
def entrada_dados():
    dados = []
    i = 0
    while i < 2:
        dados.append(int(input(f'\nDigite a parcela {i+1}:')))
        i+=1
    return dados
    
# Definição da função soma
def soma (numero_1,numero_2):
    resultado = numero_1 + numero_2
    return resultado

# Definição da função saída
def saida_dados(x):
    print(f'\nO resultado da soma das parcelas digitadas é {x}')
    
def main():
    dados = entrada_dados()
    resultado = soma(dados[0], dados[1])
    saida_dados(resultado)
   
# execução da função principal
main()