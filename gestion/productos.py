import tkinter as tk
from tkinter import messagebox
class Producto:
    def __init__(self):
        self.lista_productos_prestamo = ["betonero", "Lijadora concreto", "Placa compactadora"]
        self.ventana_product = tk.Tk()
        self.ventana_product.geometry("350x450")
        self.ventana_product.title("Productos")

        self.label_nombre = tk.Label(self.ventana_product, text="Nombre Producto:")
        self.label_nombre.pack()

        self.nombre_producto = tk.Entry(self.ventana_product)
        self.nombre_producto.pack()

        self.lista_productos = tk.Listbox(self.ventana_product)
        self.lista_productos.pack()

        self.actualizar()

        self.lista_boton = tk.Button(self.ventana_product, text="Agrega", command=self.agregar)
        self.lista_boton.pack()
        self.lista_boton.config(bg='yellow')

        self.boton_borrador = tk.Button(self.ventana_product, text="Borrar", command=self.borrar)
        self.boton_borrador.config(bg='red')
        self.boton_borrador.pack()

        self.cantidad_boton = tk.Button(self.ventana_product, text="Cantidad", command=self.cantidad)
        self.cantidad_boton.pack()
        self.cantidad_boton.config(bg='blue')

        self.ventana_product.mainloop()
    def actualizar(self):
        # Llena la lista de productos en la interfaz con los productos actuales
        self.lista_productos.delete(0, tk.END)
        for producto in self.lista_productos_prestamo:
            self.lista_productos.insert(tk.END, producto)

    def agregar(self):
        new_product = self.nombre_producto.get()
        if new_product:
            # se agrega a la lista
            self.lista_productos_prestamo.append(new_product)
            self.actualizar()
            # deja en blanco la entrada del producto
            self.nombre_producto.delete(0, tk.END)

    def borrar(self):
        # aqui se selecciona con el cursor lo que se borrara de la lista
        seleccion = self.lista_productos.curselection()
        if seleccion:
            elemento = self.lista_productos.get(seleccion)
            if elemento in self.lista_productos_prestamo:
                self.lista_productos_prestamo.remove(elemento)
            self.actualizar()
    def cantidad(self):
        cantidad_productos = len(self.lista_productos_prestamo)
        messagebox.showinfo("Productos" , f' la cantidad de productos es :{cantidad_productos}')

Producto()