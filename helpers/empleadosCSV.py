import csv

def empleadosCSV(lista,listaCSV):
    with open('data/'+listaCSV,mode='w',newline='',encoding='utf-8') as empleados_csv:
        writer=csv.writer(empleados_csv)
        writer.writerow(['id','nombre','apellidos','edad', 'salario','deudas','retencionFuente','cargo','correo','telefono'])
        writer.writerows(lista)