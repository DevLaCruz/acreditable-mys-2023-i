import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo Excel
data = pd.read_excel("Recopilación_Información_BD.xlsx")
tiempos_entre_llegadas = data["Tiempo entre llegadas"]

# Calcular los resultados solicitados
max_value = tiempos_entre_llegadas.max()
min_value = tiempos_entre_llegadas.min()
mean_value = tiempos_entre_llegadas.mean()
std_dev = tiempos_entre_llegadas.std()

# Realizar el test de chi cuadrado (si aplica)
# Puedes realizar un test de chi cuadrado si tienes categorías específicas para analizar

num_data_points = len(tiempos_entre_llegadas)

# Imprimir los resultados
print("Valor máximo:", max_value)
print("Valor mínimo:", min_value)
print("Media muestral:", mean_value)
print("Desviación estándar muestral:", std_dev)
print("Número de puntos de datos:", num_data_points)

# Generar un Input Analyzer en forma de barras
plt.figure(figsize=(10, 6))
plt.hist(tiempos_entre_llegadas, bins="auto", color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Tiempo Entre Llegadas (minutos)')
plt.ylabel('Frecuencia')
plt.title('Input Analyzer - Input Analyzer de Tiempo Entre Llegadas de Encomiendas')
plt.grid(True)
plt.show()
