import tkinter
from tkinter import messagebox
from tkinter import Frame


users = {'Matias': 'mati12'}

class Usuarios_sistema:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()
        
        self.usuario = tkinter.Entry()
        self.usuario.pack()
        
        self.password = tkinter.Entry(show='*')
        self.password.pack()
        
        def login():
            user = self.usuario.get()
            contraseña = self.password.get()
            if user in users and contraseña in users[user]:
                messagebox.showinfo("inicio secion" , "iniciaste bien")
            else:messagebox.showerror("Mal","MAL")
        self.boton = tkinter.Button(root , text="Ingresa", command=login)
        self.boton.pack()
        self.boton.config(bg='green')

root = tkinter.Tk()
root.geometry("350x250")
aplicacion = Usuarios_sistema(root)
root.mainloop()