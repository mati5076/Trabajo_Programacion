import tkinter
from tkinter import messagebox

#Para iniciar secion primero debes registrarte
registrador = {'administrador': '123'}

def login():
    usuario = user.get()
    contraseña = password.get()
    if usuario in registrador and contraseña in registrador[usuario]:
        messagebox.showinfo("Inicio", "Se inicio con exito")    
    else:messagebox.showerror("Error" , 'No exist0e este usuario , Registrate')

def interfaz():
    ventana.withdraw()
    ventana_interfaz = tkinter.Tk()
    ventana_interfaz.geometry("500x450")
    ventana_interfaz.mainloop()

ventana = tkinter.Tk()
ventana.geometry("500x450")

user = tkinter.Entry()
user.pack()

password = tkinter.Entry(ventana, show='*')
password.pack()

boton = tkinter.Button(ventana, text="Iniciar secion",command=login)
boton.pack()

ventana.mainloop()