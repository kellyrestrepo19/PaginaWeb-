import pandas as pd
import matplotlib as plt


from helpers.empleadosCSV import empleadosCSV
from data.ventas import ventas
from data.crearCSV import crearCSV
from helpers.CrearTablaHTML import crearTabla
from data.empleados import empleados
from data.productos import productos

crearCSV(ventas,'ventas.csv')
empleadosCSV(empleados,'empleados.csv')
crearCSV(productos,'productos.csv')



ventasDataFrame = pd.read_csv('data/ventas.csv')
empleadosDataFrame = pd.read_csv('data/empleados.csv')
productosDataFrame = pd.read_csv('data/productos.csv')
crearTabla(ventasDataFrame, 'tablaVentas')
crearTabla(empleadosDataFrame, 'tablaEmpleados')
crearTabla(productosDataFrame, 'tablaProductos')

#print(ventasDataFrame)
#print(empleadosDataFrame)
#print(productosDataFrame)


estadisticasVentas=ventasDataFrame.head(50)
estadisticaGeneralVentas=ventasDataFrame.describe()
infoGeneralVentas=ventasDataFrame.info()

estadisticasEmpleados=empleadosDataFrame.head(50)
estadisticaGeneralEmpleados=empleadosDataFrame.describe()
infoGeneralEmpleados=empleadosDataFrame.info()
#print(estadisticasVentas)
#print(estadisticaGeneralVentas)
#print(infoGeneralVentas)
#print(estadisticasEmpleados)
#print("\n")



#4. Filtrar y ordenar(limpiar)
filtroUno=ventasDataFrame.query("(Costo>=290000) and (Costo<=300000)")
totalventas=filtroUno[['Costo','Cliente']]

#generando html con resultados del filtro
crearTabla(filtroUno,'ventasBajoCosto')



#6. Presentar y exportar los datos
ventasAltas=ventasDataFrame.nlargest(5,"Costo")
ventasBajas=ventasDataFrame.nsmallest(5,"Costo")
print(ventasBajas)

#Graficando un DATAFRAME CON MATPLOTLIB
ventasAltas["NumeroOrden"]=ventasAltas["NumeroOrden"].astype(str)
colores=['blue','green','#EFEC1B','orange','purple']
plt.figure(figsize=(10,10))
plt.bar(ventasAltas["NumeroOrden"],ventasAltas["Costo"], color=colores)

#Personalizando la gráfica

plt.xlabel("Cliente")
plt.ylabel("Costo")
plt.title("Ventas mas altas en ultimo mes")
plt.xticks(rotation=45)

rutaGrafica="figuras/barrasventa.png"
plt.savefig(rutaGrafica)
