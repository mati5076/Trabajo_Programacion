import tkinter as tk
from tkinter import messagebox
from gestion.productos import Producto
from gestion.solicitud import solicitud
from gestion.funcionario import Funcionario

class usuario_sistema:
    def __init__(self):
        self.administrador = {'205885501':'1234'}
        self.gestor_informe= {'gestor' : '1234'}
        self.funcionario = {'funcionario' : '1234'}
        
        self.ventana = tk.Tk()
        self.ventana.geometry("600x300")
        self.ventana.title("Login")
        self.ventana.config(bg='#3C3C3C')
        
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
            boton_productos.pack(pady=5)

            boton_solicitud = tk.Button(self.venta_seleccion, text='Ver Solicitudes', command=solicitud)
            boton_solicitud.pack(pady=10)

            boton_funcionario = tk.Button(self.venta_seleccion, text='Ver Funcionario', command=Funcionario)
            boton_funcionario.pack(pady=15)

            boton_cancelar = tk.Button(self.venta_seleccion, text="salir de la sesion" , command=exit)
            boton_cancelar.pack(pady=20)
        def login():
            user = self.usuario_entrada.get()
            password = self.contrasenia.get()
            if user in self.administrador and password in self.administrador[user]:
                messagebox.showinfo("Inicio" , 'Se inicio sesion')
                self.usuario_entrada.delete(0,tk.END)
                self.contrasenia.delete(0,tk.END)
                ventana_seleccion_accion()
            elif user in self.gestor_informe and password in self.gestor_informe[user]:
                messagebox.showinfo("Inicio" , 'Se( inicio sesion')
                self.usuario_entrada.delete(0,tk.END)
                self.contrasenia.delete(0,tk.END)
                ventana_seleccion_accion()
            elif user in self.funcionario and password in self.funcionario[user]:
                messagebox.showinfo("Inicio" , 'Se inicio sesion')
                self.usuario_entrada.delete(0,tk.END)
                self.contrasenia.delete(0,tk.END)
                ventana_seleccion_accion()
            else:
                messagebox.showerror("Error", "El usuario o contraseña esta mal")
                self.usuario_entrada.delete(0,tk.END)
                self.contrasenia.delete(0,tk.END)
        self.boton_inicio = tk.Button(self.ventana,text='iniciar sesion' , command=login)
        self.boton_inicio.pack()
        self.boton_inicio.config(bg='Red',font=('Calibri',10))
        
        self.boton_cancelacion = tk.Button(self.ventana, text="salir de la app" , command=exit)
        self.boton_cancelacion.pack()
        self.boton_cancelacion.config(bg='Red',font=('Calibri',10))

        self.ventana.mainloop()