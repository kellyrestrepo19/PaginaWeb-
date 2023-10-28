import csv

def productosCSV(lista,listaCSV):
    with open('data/'+listaCSV,mode='w',newline='',encoding='utf-8') as productos_csv:
        writer=csv.writer(productos_csv)
        writer.writerow(['idProducto', 'nomProducto', 'costo', 'iva'])
        writer.writerows(lista)