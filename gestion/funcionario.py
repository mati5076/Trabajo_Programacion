import tkinter as tk
from tkinter import messagebox
from gestion.solicitud import solicitud

class Funcionario:
    def __init__(self):
        self.ventana_funcionario = tk.Tk()
        self.ventana_funcionario.geometry("400x300")
        
        self.nombre_completo_label = tk.Label(self.ventana_funcionario, text="Nombre completo:")
        self.nombre_completo_label.pack()
        
        self.nombre_completo = tk.Entry(self.ventana_funcionario)
        self.nombre_completo.pack()
        
        self.run_label = tk.Label(self.ventana_funcionario , text="Run:")
        self.run_label.pack()
        
        self.run = tk.Entry(self.ventana_funcionario)
        self.run.pack()

        self.cargo_label = tk.Label(self.ventana_funcionario , text="Cargo")
        self.cargo_label.pack()

        self.cargo = tk.Entry(self.ventana_funcionario)
        self.cargo.pack()

        self.empresa_label = tk.Label(text="Empresa")
        self.empresa_label.pack()

        self.empresa = tk.Entry(self.ventana_funcionario)
        self.empresa.pack()

        opcion_contrato = ["plazo fijo","Indefinido"]
        self.tipo = tk.StringVar()
        self.tipo.set(" ")
        
        self.contrato_label = tk.Label(self.ventana_funcionario,text="Contrato:")
        self.contrato_label.pack()
        
        self.contrato = tk.OptionMenu(self.ventana_funcionario,self.tipo,*opcion_contrato)
        self.contrato.pack()

        def boton_func():
           messagebox.showinfo("Hola" , "asdasd")
           self.ventana_funcionario.withdraw()
           solicitud()

        self.boton = tk.Button(self.ventana_funcionario, text="preciona" ,command=boton_func) 
        self.boton.pack()

        self.ventana_funcionario.mainloop()