import tkinter as tk
from tkinter import messagebox
from gestion.funcionario import Funcionario

class solicitud:
    def __init__(self):
        self.ventan_solicitante = tk.Tk()
        self.ventan_solicitante.geometry("300x200")

        self.nombre_solicitante_label = tk.Label(self.ventan_solicitante,text="Nombre_solicitante")
        self.nombre_solicitante_label.pack()

        self.nombre_solicitante = tk.Entry()
        self.nombre_solicitante.pack()

        self.nombre_responsable_label = tk.Label(self.ventan_solicitante,text="Nombre_responsable:")
        self.nombre_responsable_label.pack()

        self.nombre_responsable = tk.Entry()
        self.nombre_responsable.pack()

        self.fecha_solicitante_label = tk.Label()
        self.fecha_solicitante_label.pack()

        self.fecha_solicitante = tk.Entry()
        self.fecha_solicitante.pack()

        self.fecha_devolucion_label = tk.Label()
        self.fecha_devolucion_label.pack()

        self.fecha_devolucion = tk.Entry()
        self.fecha_devolucion.pack()

        def boton_func():
           messagebox.showinfo("Hola" , "asdasd")
           Funcionario()

        self.boton = tk.Button(self.ventan_solicitante, text="preciona" ,command=boton_func) 
        self.boton.pack()
        self.ventan_solicitante.mainloop()


solicitud()