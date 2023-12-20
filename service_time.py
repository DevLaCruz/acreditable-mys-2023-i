import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns

# Cargar los datos desde el archivo Excel
data = pd.read_excel("Recopilación_Información_BD.xlsx")
tiempos_servicio = data["Tiempo de servicio"]

# Calcular los resultados solicitados
max_value = tiempos_servicio.max()
min_value = tiempos_servicio.min()
mean_value = tiempos_servicio.mean()
std_dev = tiempos_servicio.std()

# Realizar el test de chi cuadrado
num_bins = int(np.ceil(np.log2(len(tiempos_servicio)) + 1))
hist, bin_edges = np.histogram(tiempos_servicio, bins=num_bins)
observed_frequencies = hist

chi2_stat, p_value, dof, expected = chi2_contingency([observed_frequencies])

num_data_points = len(tiempos_servicio)

# Imprimir los resultados
print("Valor máximo:", max_value)
print("Valor mínimo:", min_value)
print("Media muestral:", mean_value)
print("Desviación estándar muestral:", std_dev)
print("Test de Chi cuadrado - Estadístico:", chi2_stat)
print("Test de Chi cuadrado - p-valor:", p_value)
print("Número de puntos de datos:", num_data_points)

# Generar un Input Analyzer más detallado con estimación de densidad
plt.figure(figsize=(10, 6))
sns.histplot(tiempos_servicio, bins=num_bins, kde=True, color='blue', edgecolor='black')
plt.xlabel('Tiempo de Servicio (minutos)')
plt.ylabel('Densidad / Frecuencia')
plt.title('Input Analyzer y Estimación de Densidad de Tiempos de Servicio en Encomiendas')
plt.grid(True)
plt.show()