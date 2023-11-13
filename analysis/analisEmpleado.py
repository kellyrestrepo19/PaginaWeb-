import pandas as pd
import matplotlib.pyplot as plt

from helpers.empleadosCSV import empleadosCSV
from helpers.CrearTablaHTML import crearTabla
from data.empleados import empleados

empleadosCSV(empleados,'empleados.csv')

empleadosDataFrame = pd.read_csv('data/empleados.csv',encoding='')
#print(empleadosDataFrame)

#crearTabla=(empleadosDataFrame,'tablaEmpleados')

'''estadisticasEmpleados=empleadosDataFrame.head(50)
print(estadisticasEmpleados)
print("\n")'''

# 4. Filtrar y ordenar (limpiar) según tus necesidades

filtroUno = empleadosDataFrame.query("(edad<24)")
filtroEmpleado = filtroUno[['nombre','cargo','apellidos']]
#print(filtroEmpleado)

filtroUno = empleadosDataFrame.query("(salario>2500000)")
filtroEmpleadoCuatro = filtroUno[['nombre','cargo','apellidos']]
#print(filtroEmpleadoCuatro)

crearTabla(filtroEmpleado,'empleadosJovenes')
crearTabla(filtroEmpleadoCuatro,'salariosAltos')

#6. Presentar y exportar los datos
salarioAlto=empleadosDataFrame.nlargest(10,"salario")
print(salarioAlto)

#grafica
salarioAlto["salario"]=salarioAlto['salario'].astype(str)
colores=['#33D1FF','#147FD3','#6398E8','#04199E']
plt.figure(figsize=(10,10))
plt.bar(salarioAlto["cargo"],salarioAlto["salario"], color = colores)



#Personalizando la gráfica

plt.xlabel("Cargo")
plt.ylabel("salario")
plt.title("Salarios mas altas")
#plt.xticks(rotation=45)
rutaGrafica ="figuras/barraSalario.png"
plt.savefig(rutaGrafica)