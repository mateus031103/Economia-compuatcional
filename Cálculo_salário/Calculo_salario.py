"""
Calculador de salário
Descrição: Este programa calcula o salário bruto e líquido de um trabalhador a partir da informação de horas trabalhadas, assim como a quantidade imposto que deve ser paga.
Autor: Mateus Chassot Valandro
Data:19/04/2024
Versão:0.0.1
"""
# Alocação de Memória
horas_trabalhadas: float = 0
salario_liquido: float = 0
salario_bruto: float = 0
imposto: float = 0

# Entrada de dados
horas_trabalhadas = float(input("quantas horas você trabalhou?"))

# Processamento de Dados
salario_bruto = horas_trabalhadas*40
imposto = salario_bruto*0.3
salario_liquido = salario_bruto - imposto

# Saída de dados
print(f"\nSeu salário bruto foi de {salario_bruto} reias.")
print(f"\nSeu salário líquido foi de {salario_liquido} reais.")
print(f"\nA quantidade de imposto paga foi de {imposto} reais")