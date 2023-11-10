import tkinter
from tkinter import messagebox

#Para iniciar secion primero debes registrarte
registrador = {'administrador': '123'}

def login():
    usuario = user.get()
    contraseña = password.get()
    if usuario in registrador and contraseña in registrador[usuario]:
        messagebox.showinfo("Inicio", "Se inicio con exito")    
    else:messagebox.showerror("Error" , 'No existe este usuario , Registrate')

ventana = tkinter.Tk()
ventana.geometry("500x450")

user = tkinter.Entry()
user.pack()

password = tkinter.Entry(ventana, show='*')
password.pack()

boton = tkinter.Button(ventana, text="Iniciar secion",command=login)
boton.pack()

if 'administrador' in registrador:
    pass

ventana.mainloop()