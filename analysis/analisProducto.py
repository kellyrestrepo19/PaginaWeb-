import pandas as pd


from helpers.productosCSV import productosCSV
from data.productos import productos

productosCSV(productos,'productos.csv')
productosCSV(productos,'ventas.csv')
#print(productosDataFrame)

productosDataFrame = pd.read_csv('data/productos.csv')
#print(productosDataFrame)

estadisticasProductos=productosDataFrame.head(50)
#print(estadisticasProductos)
#print("\n")