import tkinter as tk
from tkinter import messagebox
from gestion.productos import Producto
from gestion.solicitud import solicitud
from gestion.funcionario import Funcionario

class usuario_sistema:
    def __init__(self):
        self.administrador = {'administrador':'1234'}
        self.gestor_informe= {'gestor' : '321'}
        self.funcionario = {'funcionario' : '12345'}
        
        self.ventana = tk.Tk()
        self.ventana.geometry("400x250")
        self.ventana.title("Login")
        self.ventana.config(bg='black')
        
        self.label_usuario = tk.Label(text="Usuario:")
        self.label_usuario.pack()
        self.label_usuario.config(bg='black' ,fg="white")

        self.usuario_entrada = tk.Entry()
        self.usuario_entrada.pack()
        self.usuario_entrada.config(bg='black',fg='white' ,font=("Calibri",12))

        self.label_contrasenia = tk.Label(text="Contraseña:")
        self.label_contrasenia.pack()
        self.label_contrasenia.config(bg='black' , fg="white")

        self.contrasenia= tk.Entry(show='*')
        self.contrasenia.pack()
        #el font es para poder cambiar el tipo de letra y bg es ponerle color al fondo de la entrada de datos
        self.contrasenia.config(bg='black',fg='white' ,font=('Calibri',12))

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
        boton_inicio.config(bg='Red',font=('Arial',10))

        self.ventana.mainloop()