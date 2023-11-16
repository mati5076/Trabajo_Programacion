import tkinter as tk

class solicitud:
    def __init__(self):
        self.ventan_solicitante = tk.Tk()
        self.ventan_solicitante.geometry("300x300")

        self.nombre_archivo_label =tk.Label(self.ventan_solicitante , text='INgresa nombre del archivo:')
        self.nombre_archivo_label.pack()

        self.nombre_archivo = tk.Entry(self.ventan_solicitante)
        self.nombre_archivo.pack()

        self.nombre_solicitante_label = tk.Label(self.ventan_solicitante,text="Nombre_solicitante")
        self.nombre_solicitante_label.pack()

        self.nombre_solicitante = tk.Entry(self.ventan_solicitante)
        self.nombre_solicitante.pack()

        self.nombre_responsable_label = tk.Label(self.ventan_solicitante,text="Nombre_responsable:")
        self.nombre_responsable_label.pack()

        self.nombre_responsable = tk.Entry(self.ventan_solicitante)
        self.nombre_responsable.pack()
        
        self.producto_label_solicitado = tk.Label(self.ventan_solicitante , text='Solicitar el Producto')
        self.producto_label_solicitado.pack()

        self.producto_solicitado = tk.Entry(self.ventan_solicitante)
        self.producto_solicitado.pack()

        self.fecha_solicitante_label = tk.Label(self.ventan_solicitante , text="fecha")
        self.fecha_solicitante_label.pack()

        self.fecha_solicitante = tk.Entry(self.ventan_solicitante)
        self.fecha_solicitante.pack()

        self.fecha_devolucion_label = tk.Label(self.ventan_solicitante,text="devuelve")
        self.fecha_devolucion_label.pack()

        self.fecha_devolucion = tk.Entry(self.ventan_solicitante)
        self.fecha_devolucion.pack()
        
        #en esta funcion crea y guarda al momento un archivo con la extension txt
        def guardar_txt():
            archivo = self.nombre_archivo.get()
            nombre_solicitante  = self.nombre_solicitante.get()
            nombre_responsable = self.nombre_responsable.get()
            producto_solicitados = self.producto_solicitado.get()
            fecha_solicitante = self.fecha_solicitante.get()
            fecha_devolucion = self.fecha_devolucion.get()
            #permite que en el codigo  se cree un txt y escribiendo en el de manera inmediata
            with open(f'{archivo}.txt' , 'w') as arch:
                arch.write(f"Nombre solicitante :{nombre_solicitante}")
                arch.write(f"\nNombre responsable : {nombre_responsable}")
                arch.write(f'\nNombre producto : {producto_solicitados}')
                arch.write(f"\nFecha solicitud : {fecha_solicitante}")
                arch.write(f"\nFecha devolucion : {fecha_devolucion}")
        #boton que ejecuta la funcion de guardar el txt
        self.boton_archivo = tk.Button(self.ventan_solicitante , text="Guarda datos" , command=guardar_txt)
        self.boton_archivo.pack()
        
        self.ventan_solicitante.mainloop()