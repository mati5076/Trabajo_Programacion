import tkinter as tk
from tkinter import messagebox
from gestion.productos import Producto
usuarios = {'admin':'123'}

class usuario_sistema:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("250x250")
        self.ventana.title("Usuarios/login")
        self.ventana.config(bg='#616161')

        self.label_usuario = tk.Label(text="Usuario:")
        self.label_usuario.pack()
        self.label_usuario.config(bg='#616161')

        self.usuario_entrada = tk.Entry()
        self.usuario_entrada.pack()
        self.usuario_entrada.config(bg='#616161',font=("Arial",12))

        self.label_contrasenia = tk.Label(text="Contraseña:")
        self.label_contrasenia.pack()
        self.label_contrasenia.config(bg='#616161')

        self.contrasenia= tk.Entry(show='*')
        self.contrasenia.pack()
        #el font es para poder cambiar el tipo de letra y bg es ponerle color al fondo de la entrada de datos
        self.contrasenia.config(bg='#616161',font=('Arial',12))

        def login():
            user = self.usuario_entrada.get()
            password = self.contrasenia.get()
            if user in usuarios and password in usuarios[user]:
                messagebox.showinfo("Inicio" , 'Se inicio sesion')
                self.ventana.withdraw()
                Producto()
        boton_inicio = tk.Button(self.ventana,text='iniciar sesion' , command=login)
        boton_inicio.pack()
        boton_inicio.config(bg='green')
        self.ventana.mainloop()

usuario_sistema()