import pandas as pd
import matplotlib.pyplot as plt

from helpers.productosCSV import productosCSV
from helpers.CrearTablaHTML import crearTabla
from data.productos import productos

productosCSV(productos,'productos.csv')
#print(productosDataFrame)

productosDataFrame = pd.read_csv('data/productos.csv',encoding='')
#print(productosDataFrame)

#crearTabla=(productosDataFrame,'tablaProductos')

'''estadisticasProductos=productosDataFrame.head(50)
print(estadisticasProductos)
print("\n")'''

# 4. Filtrar y ordenar (limpiar) según tus necesidades

filtroUno = productosDataFrame.query("(costo>500000)")
filtroProducto = filtroUno[['idProducto','nomProducto','costo']]
#print(filtroProducto)

filtroDos = productosDataFrame.query("(costo>0) and (costo<250000)")
filtroProducto = filtroDos[['idProducto','nomProducto','costo']]
#print(filtroProductoDos)

#6. Presentar y explorar losd datos
crearTabla(filtroProducto,'productosAltosCostos')
crearTabla(filtroProducto,'productosBajoCosto')

productoBarato=productosDataFrame.nsmallest(7,"costo")
print(productoBarato)
#grafica
productoBarato["costo"]=productoBarato['costo'].astype(str)
colores=['#33D1FF','#147FD3','#6398E8','#04199E']
plt.figure(figsize=(10,10))
plt.bar(productoBarato["nomProducto"],productoBarato["costo"], color = colores)



#Personalizando la gráfica

plt.xlabel("Producto")
plt.ylabel("Costo")
plt.title("Productos mas baratos")
#plt.show()
#plt.xticks(rotation=45)
rutaGrafica ="figuras/barraProducto.png"
plt.savefig(rutaGrafica)

