import tkinter as Ventana

#********* Clase del Patron Vista.........*************************
class Vista:
    def __init__(self):
        self.miFormulario=Ventana.Tk()
        self.miFormulario.title("Formulario Registro Cliente")
        
        self.LabelNombre=Ventana.Label(self.miFormulario, text="Nombre del Cliente: ")
        self.LabelNombre.pack()
       
        self.EntryNombre=Ventana.Entry(self.miFormulario)
        self.EntryNombre.pack()
        
        self.BotonEnviar=Ventana.Button(self.miFormulario, text="Enviar")
        self.BotonEnviar.pack()
        
# *********** Zona de metodos de la clase ************************    
    # Metodo que tomas los datos de los Entry para almacenarlos en Variables locales del metodo
    def TomarDatos(self):
        auxNombre=self.EntryNombre.get()
        
    def InicioVentanas(self):
       self.miFormulario.mainloop()
        
        
        
        
#********* Clase que ejecuta el codigo General.........*************************
class CodigoPrincipal:
    def __init__(self):
        ObjVista=Vista()
        ObjVista.InicioVentanas()
        
        

# ****************** Codigo Main del Programa *********************
    
            
main=CodigoPrincipal()
    



