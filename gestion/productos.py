import tkinter as tk
from tkinter import messagebox
import pymysql

class Producto:
    def __init__(self):
        self.lista_productos_prestamo = ["betonero", "Lijadora concreto", "Placa compactadora" , "Martillo" , "bentano"]
        self.ventana_product = tk.Tk()
        self.ventana_product.geometry("600x400")
        self.ventana_product.title("Productos")
        
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='gestor_arriendo'
            )
            self.cursor = self.connection.cursor()
            print("Se incio sesion con exito")
        except Exception as e:
            print("Error",{e})

        self.id_producto_label = tk.Label(self.ventana_product, text="ID producto")
        self.id_producto_label.pack()

        self.id_producto = tk.Entry(self.ventana_product)
        self.id_producto.pack()

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

        self.cantidad_boton = tk.Button(self.ventana_product, text="Cantidad", command=self.cantidad_ventana)
        self.cantidad_boton.pack()
        self.cantidad_boton.config(bg='blue')

        self.atrapar_articulo_prestado = ''

        self.ventana_product.mainloop()

    def actualizar(self):
        self.id_producto.delete(0,tk.END)
        self.nombre_producto.delete(0, tk.END)
        # Limpiar y volver a llenar la lista_productos
        self.lista_productos.delete(0, tk.END)
        productos = self.base_listado()
        estado = self.estado()
        for producto in productos:
            for estado_id in estado:
                    if not estado_id[0] == producto[0]:
                        self.lista_productos.insert(tk.END, f"{producto[0]}: {producto[1]}: Activo")
                    elif estado_id[0] == producto[0]:
                        self.lista_productos.insert(tk.END, f"{producto[0]}: {producto[1]}: {estado_id[1]}")

    def base_listado(self):
        sql = 'SELECT id_producto,nombre_producto FROM producto'
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print("Error", e)
    
    def estado(self):
        sql = 'SELECT id_solicitud,estado FROM solicitud'
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print("Error", e)
    
    def agregar(self):
        id_producto = int(self.id_producto.get())
        new_product = self.nombre_producto.get()
        sql =  'INSERT INTO producto (id_producto , nombre_producto) VALUES(%s, %s)'
        try:
            self.cursor.execute(sql,(id_producto,new_product))
            self.connection.commit()
            messagebox.showinfo("Producto_actualizados" , "Se agrego correctamente")
            self.actualizar()
            print("se subio")
        except Exception as e:
            print("error" ,e)

    def borrar(self):
        id_producto = int(self.id_producto.get())
        sql = 'DELETE FROM producto WHERE id_producto = %s'
        try:
            self.cursor.execute(sql,(id_producto))
            self.connection.commit()
            print("Se Borro")
            messagebox.showinfo("Se borro" , "Se borro correctamente")
            self.actualizar()
        except Exception as e:
            print("Error",e)
    

    def cantidad_ventana(self):
        self.ventana_cantidad = tk.Tk()
        self.ventana_cantidad.geometry("600x400")

        self.nombre_producto_cantidad_label = tk.Label(self.ventana_cantidad,text="Nombre del producto :")
        self.nombre_producto_cantidad_label.pack()

        self.nombre_producto_cantidad = tk.Entry(self.ventana_cantidad)
        self.nombre_producto_cantidad.pack()
        
        self.cantidad_boton = tk.Button(self.ventana_cantidad, text="Cantidad", command=self.cantidad)
        self.cantidad_boton.pack()
        self.cantidad_boton.config(bg='blue')

        self.ventana_cantidad.mainloop()

    def cantidad(self):
        cantidad_nombre = self.nombre_producto_cantidad.get()
        sql = 'SELECT COUNT(*) FROM producto WHERE nombre_producto = %s'
        try:
            self.cursor.execute(sql,(cantidad_nombre))
            resutlado = self.cursor.fetchone()
            if resutlado:
                contador = resutlado[0]
                messagebox.showinfo("COntador",f"{contador}")
        except Exception as e:
            print("Error",e)
