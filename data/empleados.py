import random
empleados = []
for _ in range(2000):
    id = random.randint(1,2000)
    nombre = random.choice([
        "Juan", "María", "Carlos", "Ana", "Luis", "Laura", "Pedro", "Isabel", "Sergio", "Carmen", "Diego", "Elena", "Miguel", "Natalia", "Javier",
        "Sara", "Ricardo", "Pilar", "Gustavo", "Lorena", "Francisco", "Lucía", "Alejandro", "Raquel", "Roberto", "Beatriz", "Antonio", "Sofía",
        "Fernando", "Patricia", "David", "Susana", "Manuel", "Rosa", "José", "Verónica", "Andrés", "Olga", "Jorge", "Luisa", "Alberto", "Raúl",
        "Daniel", "Eva", "Guillermo", "Marta", "Federico", "Silvia", "Rafael", "Victoria", "Héctor", "Adriana", "Armando", "Teresa", "Gonzalo",
        "Alicia", "Óscar", "Marina", "Nacho", "Marcela", "Fabián", "Valentina", "Rodrigo", "Camila", "Joaquín", "Roxana", "Hugo", "Mariana", "Iván",
        "Gabriela", "Emilio", "Esther", "Ariel", "Clara", "Lorenzo", "Luisana", "Hernán", "Yolanda", "Simón", "Miriam", "Nicolás", "Natalie", "Sebastián",
        "Elisa", "Felipe", "Aurora", "Arturo", "Irene", "Walter", "Paula", "Eduardo", "Inés", "Julián", "Regina", "Eduardo", "Julia", "Mauricio", "Cecilia",
        "Víctor", "Patricia", "Joaquín", "Lourdes", "Ernesto", "Linda", "Rogelio", "Carla", "Gerardo", "Elvira", "Mariano", "Selena", "Alex", "Luciana", "Tomás",
        "Mónica", "Lorenzo", "Marisol", "César", "Daniela", "Omar", "Clara", "Samuel", "Liliana", "Ángel", "Gloria", "Simón", "Valeria", "Mateo", "Nancy",
        "Rogelio", "Martha", "Santiago", "Lourdes", "Juan Pablo", "Rosa María", "Fernando", "Carolina", "Álvaro", "Rocio", "Pablo", "Virginia", "José Luis",
        "Monica", "Diego", "Daniela", "Sergio", "Liliana", "Julián", "Sandra", "Felipe", "Diana", "Cristian", "Yolanda", "Erick", "Isabella", "Néstor", "Michelle",
        "Iván", "Alejandra", "Ricardo", "Claudia", "Mauricio", "Sylvia", "Ramón", "Guadalupe", "Marcos", "Patricia", "Cristóbal", "Gisela", "Roberto",
        "Ruth", "Jaime", "Alma", "Adrián", "Cristina", "Edgar", "Dulce", "Jesús", "Rosa", "Eduardo", "Camilo", "René", "Elsa", "Mariano", "Verónica", "Nadia",
        "Julio", "Esperanza", "Raúl", "Amparo", "Diego", "Paola", "José Miguel", "Eugenia", "Gustavo", "María Elena", "Esteban", "Susana", "César", "Pamela",
        "Luis Miguel", "Ximena", "Santiago", "Lucero", "Martín", "Selene", "Joaquín", "Isis", "Alberto", "Magdalena", "Manuel", "Alicia", "Leonardo", "Laura",
        "Francisco Javier", "Fabiola"
    ])
    
    apellidos = random.choice([
        "Pérez González", "López Martínez", "Rodríguez Sánchez", "González Fernández", "Ramirez Torres", "Torres Morales", "Reyes Rivera",
        "Díaz Herrera", "Medina Ortega", "Castro Soto", "Paredes Romero", "Jiménez Ruiz", "Espinosa Herrera", "Navarro Cordero", "Acosta Aguilar",
        "Delgado Valenzuela", "Ríos Rojas", "Vargas Molina", "Araya Bravo", "Campos Mendoza", "Jara Silva", "Rojas Vargas",
        "Torres Morales", "Pérez González", "Rodríguez Martínez", "Sánchez López", "López Fernández", "Ramirez Torres", "Torres Morales",
        "Reyes Rivera", "Díaz Herrera", "Medina Ortega", "Castro Soto", "Soto Romero", "Paredes Jiménez", "Jiménez Ruiz", "Ruiz Espinosa",
        "Espinosa Herrera", "Herrera Navarro", "Navarro Cordero", "Cordero Acosta", "Acosta Aguilar", "Aguilar Delgado", "Delgado Valenzuela",
        "Valenzuela Ríos", "Ríos Rojas", "Rojas Vargas", "Vargas Molina", "Molina Araya", "Araya Bravo", "Bravo Campos", "Campos Mendoza", "Mendoza Jara",
        "Jara Silva", "Silva Rojas", "Rojas Vargas", "Vargas Torres", "Torres Morales", "Morales Pérez", "Pérez González", "Gallego Henao", "Giraldo Pacheco",
        "Ceron Restrepo", "Mejis Yepez", "Patiño Ceron", "Henao Carvajal", "Mejia Tobon", "Ochoa Ospina", "Hernandez Pulgarin"
    ])
    
    edad = random.randint(18, 50)
    salario = random.randint(3000000, 15000000)
    cargo = random.choice(["Avanzado","Desarrollador","Intermedio","Arquitecto","Junior"])
    deudas = random.choice([True, False])
    retencionFuente = round(random.uniform(0.1, 10.0), 2)
    correo = random.choice([
        "juanperez@grupoUribe.com","marialopez@grupoUribe.com","carlos.rodri@grupoUribe.com","ana.gonzalez@grupoUribe.com",
        "luis.ramirez@grupoUribe.com","laura.torres@grupoUribe.com","pedro.gonzal@grupoUribe.com","isabel.perez@grupoUribe.com",
        "sergio.garci@grupoUribe.com","carmen.martinez@grupoUribe.com","diego.sanchez@grupoUribe.com","elena.fernandez@grupoUribe.com",
        "miguel.ramirez@grupoUribe.com","natalia@grupoUribe.com","javier.gonzalez@grupoUribe.com","perez@grupoUribe.com",
        "ricardo.garcia@grupoUribe.com","pilar@grupoUribe.com","gustavo.sanchez@grupoUribe.com","lorena.lopez@grupoUribe.com",
        "ana16@gripoUribe.com","hector87@grupo"])
    telefono = random.choice([
        '313093317', '339497552', '333657021', '303800669', '327097099', '339135269', '316628259', '325917474',
        '318629660', '324825733', '323607712', '316048687', '311120866', '327860472', '326597842', '313794721', 
        '338990387', '328301572', '308744506', '327044559', '332416850', '308051136', '324790359', '306008925',
        '336557553', '307928648', '311690843', '312698939', '331156443', '309906353', '324937816', '313031560',
        '333552383', '312408592', '336785801', '334428609', '319047525', '306348747', '306623656', '326565440',
        '339219329', '315226314', '324866538', '309467299', '319966724', '308126436', '315693329', '308045929', 
        '329035787', '317916910', '301322584', '302969219', '312244732', '331847489', '312722281', '329326917', 
        '308255537', '335646315', '309470013', '325079221', '305910821', '312208163', '327880066', '337628116', 
        '324438547', '323103945', '312167897', '311260842', '302250636', '325752126', '334932009', '311055863',
        '336343003', '336424584', '326251316', '325786277', '301165494', '316125965', '331781835', '332707078',
        '301480959', '335326763', '338907440', '324399307', '327466628', '335473332', '318005074', '335630349',
        '328491061', '325322980', '304442897', '327814237', '314856563', '318975656', '307955912', '331726846',
        '316510808', '336371350', '304213606', '306586235'])
    empleado = [id,nombre,apellidos,edad, salario,deudas,retencionFuente,cargo,telefono]
    empleados.append(empleado)
   