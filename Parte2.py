import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
from scipy.stats import cauchy

def generar_uniforme(a, c, m, semilla, n):
    valores = []
    sem = semilla
    for _ in range(n):
        sem = (a * sem + c) % m
        valores.append(sem / m)
    return valores

def simulador_cauchy(uniformes):
    muestras_cauchy = []
    for u in uniformes:
        x = math.tan(math.pi * (u - 0.5))
        muestras_cauchy.append(x)
    return muestras_cauchy

def main():
    a = 1664525
    c = 1013904223
    m = 2**32
    #semilla = 123456789
    semilla = int(time.time())
    n = 100

    varContUniforme = generar_uniforme(a, c, m, semilla, n)

    #Grafica histograma y densidad de la variable uniforme
    sns.histplot(varContUniforme, bins=10, kde=True, stat='density', color='blue')
    plt.title("Uniforme continua [0,1] - Histograma y Densidad")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.grid(True)
    plt.show()

    variableCauchy = simulador_cauchy(varContUniforme)

    #Grafica histograma y densidad estimada de la variable Cauchy
    sns.histplot(variableCauchy, bins=50, kde=True, stat='density', color='red', label="Densidad estimada")

    #Superpone la densidad teórica de Cauchy estándar
    x_vals = np.linspace(-10, 10, 1000)
    plt.plot(x_vals, cauchy.pdf(x_vals), 'k--', label='Densidad teórica Cauchy(0,1)')

    plt.title("Variable Aleatoria Cauchy Estándar")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(True)
    plt.xlim(-10, 10)
    plt.show()

if __name__ == "__main__":
    main()
