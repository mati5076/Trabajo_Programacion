import tkinter as tk
from tkinter import messagebox
from gestion.productos import Producto
usuarios = {'admin':'123'}

class usuario_sistema:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("250x250")

        self.label_usuario = tk.Label(text="Usuario:")
        self.label_usuario.pack()

        self.usuario_entrada = tk.Entry()
        self.usuario_entrada.pack()

        self.label_contrasenia = tk.Label(text="Contraseña:")
        self.label_contrasenia.pack()

        self.contrasenia= tk.Entry(show='*')
        self.contrasenia.pack()

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
