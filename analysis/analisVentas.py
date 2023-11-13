import pandas as pd
import matplotlib.pyplot as plt

from helpers.ventasCSV import ventaCSV
from helpers.CrearTablaHTML import crearTabla
from data.ventas import ventas

ventaCSV(ventas,'ventas.csv')

ventasDataFrame = pd.read_csv('data/ventas.csv',encoding='')
#print(ventasDataFrame)

#crearTabla(ventasDataFrame,'tablaventas')

#estadisticasVentas=ventasDataFrame.head(50)
#print(estadisticasVentas)
#print("\n")

#4. Filtrar y ordenar(limpiar)
filtroUno=ventasDataFrame.query("(costo>=290000) and (costo<=300000)")
print(filtroUno)
totalventas=filtroUno[['costo','producto']]
print(totalventas)


