import pandas as pd


from helpers.empleadosCSV import empleadosCSV
from data.empleados import empleados

empleadosCSV(empleados,'empleados.csv')

empleadosDataFrame = pd.read_csv('data/empleados.csv')
#print(empleadosDataFrame)

estadisticasEmpleados=empleadosDataFrame.head(50)
print(estadisticasEmpleados)
print("\n")


