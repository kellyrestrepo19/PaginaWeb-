import random
productos = []
for _ in range(3000):
    idProducto=random.randint(0,1000)
    nomProducto=random.choice(['Camisa Polo', 'Chaqueta Cuero Dama', 'Buso', 'Correa','Camisa Basica','Gorra','Termo','Blusa','Vestido',
                               'Pantalon', 'Short', 'Sudadera','Pantaloneta','Medias Tobilleras','Medias Largas','Cordones','Camisa Cuello V',
                               'Zapatos','Chaqueta Cuero Caballero', 'Pines (accesorios)','Bono Regalo','Reloj Dama','Reloj Caballero',
                               "Camiseta básica","Pantalones vaqueros","Zapatos deportivos","Vestido elegante","Corbata de seda","Sombrero de verano",
                               "Bufanda de lana","Reloj de pulsera","Gafas de sol","Calcetines de algodón","Cinturón de cuero","Bolso de mano","Camisa a rayas",
                               "Chaqueta de cuero","Vestido de noche","Botas de montaña","Blusa de seda","Anillo de diamantes","Pantalones cortos",
                               "Bikini","Chaqueta de invierno","Gorro de lana","Pantalones de yoga","Jersey de lana","Zapatos de tacón","Traje de baño",
                               "Chaleco acolchado","Camiseta polo","Zapatillas de casa","Sudadera con capucha","Camiseta de tirantes","Chándal","Pañuelo de seda",
                               "Zapatos de vestir","Mochila","Sudadera ligera","Falda plisada","Chaqueta vaquera","Gorro de esquí","Mono corto","Pijama de algodón",
                               "Pantalones cargo","Vestido de verano","Zapatos de lona","Blusa estampada","Cartera","Shorts de playa","Gorros de baño",
                               "Leggings deportivos",
                               "Abrigo largo"
])
    costo = random.randint(150000, 600000)
    iva=random.randint(0,19)
    pt = [idProducto, nomProducto, costo, (costo*iva)]
    productos.append(pt)
    print(productos)