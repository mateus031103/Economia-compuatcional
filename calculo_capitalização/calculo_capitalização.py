"""
Calculador de Capitalização
Descrição: Este programa calcula a capitalização de um investimento a partir da sua taxa de juros e o tempo investido.
Autor: Mateus Chassot Valandro
Data:19/04/2024
Versão:0.0.1
"""

# Alocação de Memória
capital: float = 0
taxa_juros: float = 0
periodo: int = 0
retorno = 0
montante: float = 0
# Entrada de dados
capital = float(input("Qual o valor investido?"))
taxa_juros = float(input("Qual a taxa de juros do investimento?"))
periodo = int(input("Quanto tempo o dinheiro ficará investido?"))
# Processamento de Dados
montante = (capital * ( 1.0 + taxa_juros) ** periodo)
retorno = montante - capital
# saida de dados
print(f"\nseu retorno será de {montante} reais")
print(f"\n seu lucro foi de {retorno} reais")