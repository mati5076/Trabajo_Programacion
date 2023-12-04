import tkinter as tk
from tkinter import messagebox

class Funcionario:
    def __init__(self):
        self.ventana_funcionario = tk.Tk()
        self.ventana_funcionario.geometry("400x300")
        self.ventana_funcionario.title('Funcionario')
        
        self.nomnbre_txt_label = tk.Label(self.ventana_funcionario , text="Nombre txt")
        self.nomnbre_txt_label.pack()
        
        self.nomnbre_txt = tk.Entry(self.ventana_funcionario)
        self.nomnbre_txt.pack()

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

        self.empresa_label = tk.Label(self.ventana_funcionario,text="Empresa")
        self.empresa_label.pack()

        self.empresa = tk.Entry(self.ventana_funcionario)
        self.empresa.pack()

        opcion_contrato = ["plazo fijo","Indefinido"]
        self.tipo = tk.StringVar()
        self.tipo.set("Selecciona")
        
        self.contrato_label = tk.Label(self.ventana_funcionario,text="Contrato:")
        self.contrato_label.pack()
        
        self.contrato = tk.OptionMenu(self.ventana_funcionario,self.tipo,*opcion_contrato)
        self.contrato.pack()
   
        #en esta funcion crea y guarda al momento un archivo con la extension txt
        def guardar_txt():
            archivo =  self.nomnbre_txt.get()
            nombre_empleado = self.nombre_completo.get()
            rut = self.run.get()
            cargo = self.cargo.get()
            empresa = self.empresa.get()
            contrato = self.tipo.get()
            #permite que en el codigo  se cree un txt y escribiendo en el de manera inmediata
            with open(f'{archivo}.txt' , 'w') as arch:
                arch.write(f"Nombre Completo empleado : {nombre_empleado}")
                arch.write(f"\nRut : {rut}")
                arch.write(f'\nCargo : {cargo}')
                arch.write(f"\nEmpresa : {empresa}")
                arch.write(f"\nContrato : {contrato}")
                 #boton que ejecuta la funcion de guardar el txt
        self.boton_archivo = tk.Button(self.ventana_funcionario , text="Guarda datos" , command=guardar_txt)
        self.boton_archivo.pack()
        
        self.ventana_funcionario.mainloop()