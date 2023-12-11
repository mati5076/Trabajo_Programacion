import tkinter as tk
import pymysql

class solicitud:
    def __init__(self):
        self.ventan_solicitante = tk.Tk()
        self.ventan_solicitante.geometry("600x400")
        self.ventan_solicitante.title("Solicitud")
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user="root",
                password='',
                db='gestor_arriendo'
            )
            self.cursor = self.connection.cursor()
        except Exception as ex :
            print(f"Error {ex}")
        self.id_label =tk.Label(self.ventan_solicitante , text='ID')
        self.id_label.pack()

        self.id_solicitud = tk.Entry(self.ventan_solicitante)
        self.id_solicitud.pack() 

        self.nombre_solicitante_label = tk.Label(self.ventan_solicitante,text="Nombre_solicitante")
        self.nombre_solicitante_label.pack()

        self.nombre_solicitante = tk.Entry(self.ventan_solicitante)
        self.nombre_solicitante.pack()

        self.nombre_responsable_label = tk.Label(self.ventan_solicitante,text="Nombre_responsable:")
        self.nombre_responsable_label.pack()

        self.nombre_responsable = tk.Entry(self.ventan_solicitante)
        self.nombre_responsable.pack()
        
        self.producto_label_solicitado = tk.Label(self.ventan_solicitante , text='Solicitar el Producto')
        self.producto_label_solicitado.pack()

        self.producto_solicitado = tk.Entry(self.ventan_solicitante)
        self.producto_solicitado.pack()

        self.fecha_solicitante_label = tk.Label(self.ventan_solicitante , text="fecha")
        self.fecha_solicitante_label.pack()

        self.fecha_solicitante = tk.Entry(self.ventan_solicitante)
        self.fecha_solicitante.pack()

        self.fecha_devolucion_label = tk.Label(self.ventan_solicitante,text="devuelve")
        self.fecha_devolucion_label.pack()

        self.fecha_devolucion = tk.Entry(self.ventan_solicitante)
        self.fecha_devolucion.pack()
                
        self.estado_label = tk.Label(self.ventan_solicitante , text="Activo/Inactivo")
        self.estado_label.pack()

        self.estado = tk.Entry(self.ventan_solicitante)
        self.estado.pack()

        self.boton_ingresar_solicitud = tk.Button(self.ventan_solicitante, text="Subir solicitud",command=self.solicitud_productos)      
        self.boton_ingresar_solicitud.pack()

        self.boton_modificar_solicitud= tk.Button(self.ventan_solicitante, text="modificar solicitud",command=self.modificacion)      
        self.boton_modificar_solicitud.pack()
        
        self.boton = tk.Button(self.ventan_solicitante, text="Devolucion Producto", command=self.ventana_modificacion_devolucion)
        self.boton.pack()
        
        self.boton_ver = tk.Button(self.ventan_solicitante, text="Ver solicitud", command=self.ver_soliictudes)
        self.boton_ver.pack()

        self.ventan_solicitante.mainloop()
    
    def solicitud_productos(self):
        id_solicitud = int(self.id_solicitud.get())
        nombre_solicitante = self.nombre_solicitante.get()
        nombre_respo = self.nombre_responsable.get()
        producto_soli = self.producto_solicitado.get()
        fecha_soli = self.fecha_solicitante.get()
        fecha_devol = self.fecha_devolucion.get()
        estado_subir = self.estado.get()
        
        sql = 'INSERT INTO solicitud(id_solicitud , nombre_solicitante , nombre_responsable , producto_solicitado , fecha_solicitacion , fecha_devolucion,estado) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql,(id_solicitud,nombre_solicitante,nombre_respo,producto_soli,fecha_soli , fecha_devol,estado_subir))
            self.connection.commit()
            print("se Subio la solicitud")
            self.id_solicitud.delete(0,tk.END)
            self.nombre_solicitante.delete(0,tk.END)
            self.nombre_responsable.delete(0,tk.END)
            self.fecha_devolucion.delete(0,tk.END)
            self.fecha_solicitante.delete(0,tk.END)
            self.estado.delete(0,tk.END)
        except Exception as e:
            print(f"Error al insertar el valor: {e}")
            #evita los cambios a la base de datos
            self.connection.rollback()
    def modificacion(self):
        self.ventana_nueva = tk.Toplevel(self.ventan_solicitante)
        self.ventana_nueva.geometry("600x400")
        self.id_label = tk.Label(self.ventana_nueva,text="Id")
        self.id_label.pack()

        self.id_usado = tk.Entry(self.ventana_nueva)
        self.id_usado.pack()
                
        self.producto_mod_label = tk.Label(self.ventana_nueva, text="Nuevo producto")
        self.producto_mod_label.pack()

        self.producto_mod = tk.Entry(self.ventana_nueva)
        self.producto_mod.pack()
        #se modifica el nombre del producto 
        def modificacion_boton():
            id_solicitud = int(self.id_usado.get())
            new_name = self.producto_mod.get()
            sql = 'UPDATE solicitud SET producto_solicitado = %s WHERE id_solicitud = %s'
            try:
                self.cursor.execute(sql,(new_name,id_solicitud))
                self.connection.commit()
                print("Se modifico")
            except Exception as e:
                print(f"error {e}")
                self.connection.rollback()

        self.boton_subir_modificacion = tk.Button(self.ventana_nueva,text="Modificar",command=modificacion_boton)
        self.boton_subir_modificacion.pack()

    def ventana_modificacion_devolucion(self):
        self.ventana_mod = tk.Toplevel(self.ventan_solicitante)
        self.ventana_mod.geometry("600x300")
        self.id_label_estado_mod = tk.Label(self.ventana_mod, text="ID")
        self.id_label_estado_mod .pack()

        self.id_solicitud = tk.Entry(self.ventana_mod)
        self.id_solicitud.pack() 

        self.boton_estado = tk.Button(self.ventana_mod, text="Modificar Estado", command=self.estado_nuevo)
        self.boton_estado.pack()

        self.ventana_mod.mainloop()

    def estado_nuevo(self):
        id_solicitante = int(self.id_solicitud.get())
        sql = 'DELETE FROM solicitud WHERE id_solicitud = %s'
        try:
            self.cursor.execute(sql,(id_solicitante))
            self.connection.commit()
            print("Se borro ese producto fue devuelto")
        except Exception as e:
            print(f"error {e}")
            self.connection.rollback()
    def ver_soliictudes(self):
        self.ventana_solicitudes = tk.Toplevel(self.ventan_solicitante)
        self.ventana_solicitudes.geometry("600x400")  
        
        self.lista_solicitud = tk.Listbox(self.ventana_solicitudes)
        self.lista_solicitud.pack()

        self.actualizar()
    
        self.ventana_solicitudes.mainloop()

    def estado_listado(self):
        sql = 'SELECT *FROM solicitud'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def  actualizar(self):
        todo = self.estado_listado()
        for solicitacion in todo:
            self.lista_solicitud.insert(tk.END,f"{solicitacion[0]} : {solicitacion[1]} : {solicitacion[2]} : {solicitacion[3]} : {solicitacion[4] } : {solicitacion[5]} : {solicitacion[6]}")
