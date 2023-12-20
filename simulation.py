import simpy
import pandas as pd
import numpy as np

# Cargar los datos desde el archivo Excel
data = pd.read_excel("Recopilación_Información_BD.xlsx")
tiempos_llegada = data["Tiempo entre llegadas"]
tiempos_servicio = data["Tiempo de servicio"]

# Definir la función del proceso de llegada
def llegada(env, servidor):
    for i in range(len(tiempos_llegada)):
        yield env.timeout(tiempos_llegada[i])
        env.process(servicio(env, servidor, i))

# Definir la función del proceso de servicio
def servicio(env, servidor, index):
    with servidor.request() as req:
        yield req
        yield env.timeout(tiempos_servicio[index])

# Configurar y ejecutar la simulación
env = simpy.Environment()
servidor = simpy.Resource(env, capacity=2)  # Dos ventanillas

env.process(llegada(env, servidor))
env.run()

print("Simulación completada.")
