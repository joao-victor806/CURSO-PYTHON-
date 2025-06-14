# main.py

# Objetivo
# Calcular estatísticas básicas de um conjunto de dados.

# Dados

# Crie um dicionário com valores de 30 produtos:

#Tarefas
#0. Extraia para uma listas todos os valores com um loop.

# crie um arquivo separado com as funções para resolver para uma das solicitações:
#1. Calcule a média.
#2. Calcule a mediana.
#3. Calcule a moda.
#4. Calcule a variância.
#5. Calcule o desvio padrão.
#6. Calcule a amplitude.

from estatisticas import (
    calcular_media,
    calcular_mediana,
    calcular_moda,
    calcular_variancia,
    calcular_desvio_padrao,
    calcular_amplitude
)

# Dicionário com os valores dos produtos
produtos = {
    "Carro": [4000, 5600, 12000],
    "Moto": [5000, 2500, 4000],
    "Bicicleta": [70, 150, 300],
    "Avião": [25000, 40000, 50000],
    "Helicóptero": [2500, 3000, 3500],
    "Navio": [6200, 7200, 9200],
    "Barco": [7000, 10000, 13000],
    "Jetski": [900, 1500, 3500],
    "Onibus": [10000, 13000, 16000],
    "Skate": [55, 75, 85]
}

# Iterar pelos produtos e exibir estatísticas
for nome, valores in produtos.items():
    print(f"\n Estatísticas para: {nome}")
    print(f"  Média: {calcular_media(valores):.2f}")
    print(f"  Mediana: {calcular_mediana(valores):.2f}")
    print(f"  Moda: {calcular_moda(valores)}")
    print(f"  Variância: {calcular_variancia(valores):.2f}")
    print(f"  Desvio Padrão: {calcular_desvio_padrao(valores):.2f}")
    print(f"  Amplitude: {calcular_amplitude(valores):.2f}")
