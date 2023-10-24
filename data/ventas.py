import random

ventas = []
for _ in range(1000):
    
    numeroOrden= random.randint(0,300000)
    fechaOrden = random.choice(['2023-07-05', '2023-04-21', '2023-02-06', '2022-10-28', '2023-07-17', '2023-04-09', '2023-01-06',
         '2023-10-04', '2022-11-29', '2023-08-10', '2023-08-10', '2023-05-08', '2023-04-17', '2023-10-12','2022-12-31', '2023-01-09'
         '2023-05-27', '2023-02-05', '2023-09-27', '2023-01-28', '2023-01-30', '2023-04-07', '2023-08-19', '2023-07-03', '2023-05-29',
         '2023-09-08', '2023-04-20', '2023-04-24', '2023-10-22', '2023-08-10', '2023-04-25', '2023-03-07', '2022-11-06', '2022-12-26', 
         '2023-07-19', '2023-05-18', '2023-07-28', '2023-07-03', '2023-09-10', '2023-02-23', '2023-01-12', '2023-03-04', '2022-11-14', 
         '2022-11-02', '2023-06-25', '2023-01-07', '2023-02-03', '2023-03-07', '2023-08-13', '2023-03-01'])
    nombreClientes= random.choice(['Andres', 'Ana', 'Isabel', 'Pablo','Juan','kelly','Mauricio','Manuela','Veronica','Raul',"Gabriela", "Emilio", "Esther", "Ariel", "Clara", "Lorenzo", "Luisana", "Hernán", "Yolanda", "Simón", "Miriam", "Nicolás", "Natalie", "Sebastián",
        "Elisa", "Felipe", "Aurora", "Arturo", "Irene", "Walter", "Paula", "Eduardo", "Inés", "Julián", "Regina", "Eduardo", "Julia", "Mauricio", "Cecilia",
        "Víctor", "Patricia", "Joaquín", "Lourdes", "Ernesto", "Linda", "Rogelio", "Carla", "Gerardo", "Elvira", "Mariano", "Selena", "Alex", "Luciana", "Tomás",
        "Mónica", "Lorenzo", "Marisol"])
    apellidoClientes = random.choice([ "Pérez González", "López Martínez", "Rodríguez Sánchez", "González Fernández", "Ramirez Torres", "Torres Morales", "Reyes Rivera",
        "Díaz Herrera", "Medina Ortega", "Castro Soto", "Paredes Romero", "Jiménez Ruiz", "Espinosa Herrera", "Navarro Cordero", "Acosta Aguilar",
        "Delgado Valenzuela", "Ríos Rojas", "Vargas Molina", "Araya Bravo", "Campos Mendoza", "Jara Silva", "Rojas Vargas",
        "Torres Morales", "Pérez González", "Rodríguez Martínez", "Sánchez López", "López Fernández", "Ramirez Torres", "Torres Morales",
        "Reyes Rivera", "Díaz Herrera", "Medina Ortega", "Castro Soto", "Soto Romero", "Paredes Jiménez", "Jiménez Ruiz", "Ruiz Espinosa",
        "Espinosa Herrera", "Herrera Navarro", "Navarro Cordero", "Cordero Acosta", "Acosta Aguilar", "Aguilar Delgado", "Delgado Valenzuela",
        "Valenzuela Ríos", "Ríos Rojas"])
    costo = random.randint(150000, 1000000)
    orden = [numeroOrden,fechaOrden,nombreClientes,apellidoClientes, costo]
    ventas.append(orden)
print(ventas)
    
