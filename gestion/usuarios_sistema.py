import tkinter as tk
from tkinter import messagebox
from gestion.productos import Producto
from gestion.solicitud import solicitud
from gestion.funcionario import Funcionario
from gestion.grafico import grafico
import pymysql

class usuario_sistema:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x300")
        self.ventana.title("Login")
        self.ventana.config(bg='#3C3C3C')
        
        try:
            self.connection = pymysql.connect(
                host= 'localhost',
                user= 'root',
                password= '',
                db= 'gestor_arriendo'
                )

            self.cursor = self.connection.cursor()
            print("Conexion correcta")

        except Exception as ex:
            print(f'Error en la conexion', ex)
            
        self.label_usuario = tk.Label(text="Usuario:")
        self.label_usuario.pack()
        self.label_usuario.config(bg='#3C3C3C' ,fg="white")

        self.usuario_entrada = tk.Entry()
        self.usuario_entrada.pack()
        mensaje = 'Rut/Nombre usuario'
        self.usuario_entrada.insert(0,mensaje)
        self.usuario_entrada.config(bg='#3C3C3C',fg='white' ,font=("Calibri",12))

        self.label_contrasenia = tk.Label(text="Contraseña:")
        self.label_contrasenia.pack()
        self.label_contrasenia.config(bg='#3C3C3C' , fg="white")

        self.contrasenia= tk.Entry(show='*')
        self.contrasenia.pack()
        #el font es para poder cambiar el tipo de letra y bg es ponerle color al fondo de la entrada de datos
        self.contrasenia.config(bg='#3C3C3C',fg='white' ,font=('Calibri',12))

        def ventana_seleccion_accion():
            self.venta_seleccion = tk.Toplevel(self.ventana)
            self.venta_seleccion.title("Escoge que haras")
            self.venta_seleccion.geometry("600x300")

            boton_productos = tk.Button(self.venta_seleccion, text='Ver Productos', command=Producto)
            boton_productos.pack(pady=10)

            boton_solicitud = tk.Button(self.venta_seleccion, text='Ver Solicitudes', command=solicitud)
            boton_solicitud.pack(pady=20)

            boton_grafico =  tk.Button(self.venta_seleccion, text="Grafico",command=grafico)
            boton_grafico.pack()

            self.boton_contrasenia_nueva = tk.Button(self.venta_seleccion,text="cambiar contraseña" , command=self.cambio_contrasenia_ventana)
            self.boton_contrasenia_nueva.pack()

            boton_cancelar = tk.Button(self.venta_seleccion, text="salir de la sesion" , command=exit)
            boton_cancelar.pack(pady=30)
        
        def validacion():
            rut = self.usuario_entrada.get()
            nombre = self.usuario_entrada.get()
            password = self.contrasenia.get()

            try:
                sql = 'SELECT * FROM usuario WHERE (nombre_usuario = %s OR rut = %s) AND contrasenia = %s'
                self.cursor.execute(sql, (nombre, rut, password))
                validar = self.cursor.fetchone()

                if validar:
                    return True
                else:
                    return False

            except Exception as ex:
                print(f"Error : {ex}")

        def registro():
            Funcionario()

        def login():
            user = self.usuario_entrada.get()
            password = self.contrasenia.get()
            if not validacion():
                messagebox.showerror("Error", "El usuario o contraseña es incorrecto")
                self.usuario_entrada.delete(0, tk.END)
                self.contrasenia.delete(0, tk.END)
            if validacion():
                messagebox.showinfo("Inicio", f'Se inicio sesion como {user}')
                self.usuario_entrada.delete(0, tk.END)
                self.contrasenia.delete(0, tk.END)
                ventana_seleccion_accion()

        self.boton_inicio = tk.Button(self.ventana,text='iniciar sesion' , command=login)
        self.boton_inicio.pack()
        self.boton_inicio.config(bg='Red',font=('Calibri',10))
                    
        self.boton_registro = tk.Button(self.ventana,text='Registro' , command=registro)
        self.boton_registro.pack()
        self.boton_registro.config(bg='Red',font=('Calibri',10))

        self.boton_cancelacion = tk.Button(self.ventana, text="salir de la app" , command=exit)
        self.boton_cancelacion.pack()
        self.boton_cancelacion.config(bg='Red',font=('Calibri',10))
        
        self.ventana.mainloop()
        self.cerrar_base_datos()
    def cambio_contrasenia_ventana(self):
        self.ventana_contrasenia = tk.Toplevel(self.ventana)
        
        self.usuario_entrada_n = tk.Entry(self.ventana_contrasenia)
        self.usuario_entrada_n.pack()

        self.label_contrasenia = tk.Label(self.ventana_contrasenia,text="Contraseña:")
        self.label_contrasenia.pack()

        self.contrasenia_n= tk.Entry(self.ventana_contrasenia,show='*')
        self.contrasenia_n.pack()

        self.boton_cambio = tk.Button(self.ventana_contrasenia , text="Cambia contraseña" , command=self.cambio_contrasenia)
        self.boton_cambio.pack()

    def cambio_contrasenia(self):
        contrasenia_user = self.contrasenia_n.get()
        nombre_user = self.usuario_entrada_n.get()
        sql = 'UPDATE  usuario SET contrasenia = %s WHERE nombre_usuario = %s'
        try:
            self.cursor.execute(sql,(contrasenia_user,nombre_user))
            messagebox.showinfo("Exito","Se cambio la contraseña con exito")
            self.connection.commit()
        except Exception as e:
            print("Error" ,e)
            self.connection.rollback()
        
    def cerrar_base_datos(self):
        self.connection.close()
        print("se cerro conexion con exito")