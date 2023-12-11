import tkinter as tk
import pymysql

class Funcionario:
    def __init__(self):
        self.ventana_funcionario = tk.Tk()
        self.ventana_funcionario.geometry("600x400")
        self.ventana_funcionario.title('Funcionarios')
        try:
            self.connection = pymysql.connect(
                host= 'localhost',
                user= 'root',
                password= '',
                db= 'gestor_arriendo'
                )

            self.cursor = self.connection.cursor()
            print("Conexion correcta")

        except Exception as ex:
            print(f'Error en la conexion {ex}') 

        self.numero_trabajador_label = tk.Label(self.ventana_funcionario , text="ID")
        self.numero_trabajador_label.pack()
        
        self.id = tk.Entry(self.ventana_funcionario)
        self.id.pack()

        self.nombre_completo_label = tk.Label(self.ventana_funcionario, text="Nombre completo:")
        self.nombre_completo_label.pack()

        self.nombre_completo = tk.Entry(self.ventana_funcionario)
        self.nombre_completo.pack()
        
        self.contraseniaa_label = tk.Label(self.ventana_funcionario, text="Contraseña:")
        self.contraseniaa_label.pack()

        self.contraseniaa = tk.Entry(self.ventana_funcionario,show='*')
        self.contraseniaa.pack()

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
        
        self.boton = tk.Button(self.ventana_funcionario,text="Crear cuenta",command=self.insertar_trabajadores)
        self.boton.pack()
        
        self.ventana_funcionario.mainloop()
        self.cerrar_base()
    
    def insertar_trabajadores(self):

        id_usuario = int(self.id.get())
        nombre_user = self.nombre_completo.get()
        contrasenia_user = self.contraseniaa.get()
        rut_user = self.run.get()
        cargo_user = self.cargo.get()
        empresa_user = self.empresa.get()
        contrato_user = self.tipo.get()

        sql = 'INSERT INTO usuario (id_usuario, nombre_usuario, contrasenia, rut, cargo, empresa, contrato) VALUES (%s, %s, %s, %s, %s, %s, %s)'

        try:
            self.cursor.execute(sql, (id_usuario, nombre_user, contrasenia_user, rut_user, cargo_user, empresa_user, contrato_user))
            self.connection.commit()
            print("Se ingresó con éxito")
        except Exception as e:
            print(f"Error al insertar el valor: {e}")
            #evita los cambios a la base de datos
            self.connection.rollback()