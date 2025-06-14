# estatisticas.py

import statistics as stats

def calcular_media(valores):
    return stats.mean(valores)

def calcular_mediana(valores):
    return stats.median(valores)

def calcular_moda(valores):
    return stats.multimode(valores)  # Pode retornar mais de uma moda

def calcular_variancia(valores):
    return stats.variance(valores)

def calcular_desvio_padrao(valores):
    return stats.stdev(valores)

def calcular_amplitude(valores):
    return max(valores) - min(valores)
