import tkinter as tk
class Producto:
    def __init__(self):
        self.ventana_product = tk.Tk()
        self.ventana_product.geometry("350x450")
        self.ventana_product.title("Productos")

        self.label_nombre = tk.Label(self.ventana_product,text="Nombre Producto:")
        self.label_nombre.pack()

        self.nombre_producto = tk.Entry(self.ventana_product)
        self.nombre_producto.pack()

        self.lista_productos = tk.Listbox(self.ventana_product)
        self.lista_productos.pack()
        def agregar():
            new_product = self.nombre_producto.get()
            if new_product:
                #inserta
                self.lista_productos.insert(tk.END,new_product)
                #deja en blanco la entrada del producto
                self.nombre_producto.delete(0,tk.END)
        self.lista_boton = tk.Button(self.ventana_product, text="Agrega",command=agregar)
        self.lista_boton.pack()
        def borrar():
            #aqui se selecciona con el cursor lo que se borrara de la lista
            seleccion = self.lista_productos.curselection()
            if seleccion:
                self.lista_productos.delete(seleccion)
        
        self.boton_borrador = tk.Button(self.ventana_product , text="Borrar", command=borrar)
        self.boton_borrador.pack()
        self.boton_borrador.config(bg='red')
        self.ventana_product.mainloop()