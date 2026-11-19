class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Cliente(Persona):
    def __init__(self, nombre, edad, dinero, sexo,
                 color_de_pelo=None, color_de_ojos=None, numero_de_telefono=None):
        super().__init__(nombre, edad)
        self.dinero = dinero
        self.sexo = sexo
        self.color_de_pelo = color_de_pelo
        self.color_de_ojos = color_de_ojos
        self.numero_de_telefono = numero_de_telefono


class Producto:
    def __init__(self, nombre_producto, precio, stock):
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.stock = stock


def comprar_producto_cliente(cliente, producto, unidades):
    total = producto.precio * unidades
    if unidades > producto.stock:
        print("No hay suficiente stock.")
    elif cliente.dinero < total:
        print("No tienes suficiente dinero.")
    else:
        producto.stock -= unidades
        cliente.dinero -= total
        print(f"{cliente.nombre} ha comprado {unidades} unidades de {producto.nombre_producto}.")


cliente1 = Cliente("Marcos", 25, 100, "masculino")
producto1 = Producto("Camiseta", 20, 10)

comprar_producto_cliente(cliente=cliente1, producto=producto1, unidades=3)
print("Dinero restante:", cliente1.dinero)
print("Stock restante:", producto1.stock)

cliente1.color_de_pelo = "castaño"
cliente1.color_de_ojos = "marrones"
cliente1.numero_de_telefono = "600123456"
print("Color de pelo:", cliente1.color_de_pelo)
print("Color de ojos:", cliente1.color_de_ojos)
print("Número de teléfono:", cliente1.numero_de_telefono)
