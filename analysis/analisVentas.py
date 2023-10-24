import pandas as pd


from helpers.ventasCSV import ventaCSV
from data.ventas import ventas
from data.CrearCSV import crearCSV
from data.CrearTablaHTML import crearTabla

ventaCSV(ventas,'ventas.csv')



ventasDataFrame = pd.read_csv('data/ventas.csv')
#print(ventasDataFrame)


estadisticasVentas=ventasDataFrame.head(50)
print(estadisticasVentas)
print("\n")