import tkinter as tk

class Funcionario:
    def __init__(self):
        self.ventana_funcionario = tk.Tk()
        self.ventana_funcionario.geometry("400x300")
        
        self.nombre_completo_label = tk.Label(self.ventana_funcionario, text="Nombre completo:")
        self.nombre_completo_label.pack()
        
        self.nombre_completo = tk.Entry()
        self.nombre_completo.pack()
        
        self.run_label = tk.Label(self.ventana_funcionario , text="Run:")
        self.run_label.pack()
        
        self.run = tk.Entry()
        self.run.pack()

        self.cargo_label = tk.Label(self.ventana_funcionario , text="Cargo")
        self.cargo_label.pack()

        self.cargo = tk.Entry()
        self.cargo.pack()

        self.empresa_label = tk.Label(text="Empresa")
        self.empresa_label.pack()

        self.empresa = tk.Entry()
        self.empresa.pack()

        opcion_contrato = ["plazo fijo","Indefinido"]
        self.tipo = tk.StringVar()
        self.tipo.set(" ")
        
        self.contrato_label = tk.Label(text="Contrato:")
        self.contrato_label.pack()
        
        self.contrato = tk.OptionMenu(self.ventana_funcionario,self.tipo,*opcion_contrato)
        self.contrato.pack()
        self.contrato.config()
        self.ventana_funcionario.mainloop()