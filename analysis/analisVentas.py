import pandas as pd


from helpers.ventasCSV import ventaCSV
from data.ventas import ventas

ventaCSV(ventas,'ventas.csv')


ventasDataFrame = pd.read_csv('data/ventas.csv')
print(ventasDataFrame)