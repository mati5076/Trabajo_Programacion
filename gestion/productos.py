import tkinter as tk
from usuarios_sistema import usuario_sistema
class Producto:
    def __init__(self):
        self.ventana_product = tk.Tk()
        self.ventana_product.geometry("350x450")

        self.label_nombre = tk.Label(self.ventana_product,text="Nombre Producto:")
        self.label_nombre.pack()

        self.nombre_producto = tk.Entry(self.ventana_product)
        self.nombre_producto.pack()

        self.lista_productos = tk.Listbox(self.ventana_product)
        self.lista_productos.pack()

        self.ventana_product.mainloop()
