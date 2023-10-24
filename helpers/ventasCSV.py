import csv

def ventaCSV(lista,listaCSV):
    with open('data/'+listaCSV,mode='w',newline='',encoding='utf-8') as ventas_csv:
        writer=csv.writer(ventas_csv)
        writer.writerow(['numeroOrden','fechaOrden','nombreClientes','apellidoClientes','costo'])
        writer.writerows(lista)