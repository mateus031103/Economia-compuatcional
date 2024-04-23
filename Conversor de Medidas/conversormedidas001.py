"""
Programa Conversormedidas

Descrição: este programa converte metros em milimetros
Autor: Mateus Chassot Valandro
Data: 12/04/2024
Versão:0.0.1
"""
# Alocação de Memória
metros: float = 0
milimetros: float = 0

# Entrada  de Dados
metros = float(input(" digite a distância em metros: "))

# Processamento de Dados
milímetros= metros * 1000

# Saída de dados
print( f" {metros} metro(s) equivalem a {milímetros} milimetros")