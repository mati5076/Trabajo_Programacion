import tkinter as tk
from tkinter import messagebox
from gestion.productos import Producto
from gestion.solicitud import solicitud
from gestion.funcionario import Funcionario

class usuario_sistema:
    def __init__(self):
        self.administrador = {'administrador':'1234'}
        self.gestor_informe= {'gestor' : '1234'}
        self.funcionario = {'funcionario' : '1234'}
        
        self.ventana = tk.Tk()
        self.ventana.geometry("400x250")
        self.ventana.title("Login")
        self.ventana.config(bg='#3C3C3C')
        
        self.label_usuario = tk.Label(text="Usuario:")
        self.label_usuario.pack()
        self.label_usuario.config(bg='#3C3C3C' ,fg="white")

        self.usuario_entrada = tk.Entry()
        self.usuario_entrada.pack()
        self.usuario_entrada.config(bg='#3C3C3C',fg='white' ,font=("Calibri",12))

        self.label_contrasenia = tk.Label(text="Contraseña:")
        self.label_contrasenia.pack()
        self.label_contrasenia.config(bg='#3C3C3C' , fg="white")

        self.contrasenia= tk.Entry(show='*')
        self.contrasenia.pack()
        #el font es para poder cambiar el tipo de letra y bg es ponerle color al fondo de la entrada de datos
        self.contrasenia.config(bg='#3C3C3C',fg='white' ,font=('Calibri',12))

        def login():
            user = self.usuario_entrada.get()
            password = self.contrasenia.get()
            if user in self.administrador and password in self.administrador[user]:
                messagebox.showinfo("Inicio" , 'Se inicio sesion')
                self.ventana.withdraw()
                Producto()
            elif user in self.gestor_informe and password in self.gestor_informe[user]:
                messagebox.showinfo("Inicio" , 'Se inicio sesion')
                self.ventana.withdraw()
                solicitud()
            elif user in self.funcionario and password in self.funcionario[user]:
                messagebox.showinfo("Inicio" , 'Se inicio sesion')
                self.ventana.withdraw()
                Funcionario()
            else:
                messagebox.showerror("Error", "El usuario o contraseña esta mal")
                self.usuario_entrada.delete(0,tk.END)
                self.contrasenia.delete(0,tk.END)
        boton_inicio = tk.Button(self.ventana,text='iniciar sesion' , command=login)
        boton_inicio.pack()
        boton_inicio.config(bg='Red',font=('Calibri',10))

        self.ventana.mainloop()