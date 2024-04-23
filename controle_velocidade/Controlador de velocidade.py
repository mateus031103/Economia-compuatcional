"""
Controlador de Velocidade
Descrição: Este programa analisa a velocidade inserida pelo usuário, determinando se há multa e consequentemente o seu valor.
Autor: Mateus Chassot Valandro
Data:12/04/2024
Versão:0.0.1
"""
# alocação de memória
velocidade = 0
multa = 0
excedente_de_velocidade = 0
# Entrada de Dados
velocidade = int (input ("\n Qual a velocidade?  "))
# Processamento de dados
if velocidade > 80:
    excedente_de_velocidade = (velocidade - 80)
    multa = (excedente_de_velocidade*5)
else:
    print("Não há multa")
#saída de dados
if velocidade > 80:
    print (f"Sua multa é de {multa} reais.")