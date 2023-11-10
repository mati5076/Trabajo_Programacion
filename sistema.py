class Productos:
    def __init__(self,nombre_producto ,detalle , precio , cantidad , estado):
        self.nombre_producto = nombre_producto
        self.detalle = detalle
        self.precio = precio 
        self.cantidad = cantidad
        self.estado = estado



bebidas = Productos("coca" , "nose" , 12500 , 15 , "Sellado")