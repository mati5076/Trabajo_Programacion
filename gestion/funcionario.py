import tkinter as tk

class Funcionario:
    def __init__(self):
        self.ventana_funcionario = tk.Tk()
        self.ventana_funcionario.geometry("350x250")

        self.nombre_solicitante = tk.Entry()
        self.nombre_solicitante.pack()

        self.nombre_prestamo = tk.Entry()
        self.nombre_prestamo.pack()

        self.ventana_funcionario.mainloop()