import tkinter as tk

class solicitud:
    def __init__(self):
        self.ventan_solicitante = tk.Tk()
        self.ventan_solicitante.geometry("300x200")

        self.nombre_solicitante_label = tk.Label(self.ventan_solicitante,text="Nombre_solicitante")
        self.nombre_solicitante_label.pack()

        self.nombre_solicitante = tk.Entry(self.ventan_solicitante)
        self.nombre_solicitante.pack()

        self.nombre_responsable_label = tk.Label(self.ventan_solicitante,text="Nombre_responsable:")
        self.nombre_responsable_label.pack()

        self.nombre_responsable = tk.Entry(self.ventan_solicitante)
        self.nombre_responsable.pack()

        self.fecha_solicitante_label = tk.Label(self.ventan_solicitante , text="fecha")
        self.fecha_solicitante_label.pack()

        self.fecha_solicitante = tk.Entry(self.ventan_solicitante)
        self.fecha_solicitante.pack()


        self.fecha_devolucion_label = tk.Label(self.ventan_solicitante,text="devuelve")
        self.fecha_devolucion_label.pack()

        self.fecha_devolucion = tk.Entry(self.ventan_solicitante)
        self.fecha_devolucion.pack()

        self.ventan_solicitante.mainloop()