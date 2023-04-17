import tkinter as Ventana

#********* Clase del Patron Vista.........*************************
"""
    Crear una clase Vista que se encargue de presentar los datos al usuario. 
    Esta clase deberá tener métodos para mostrar formularios, campos de entrada, 
    botones y otros elementos de la interfaz de usuario. La clase Vista también deberá tener métodos
    para recibir la entrada del usuario y mostrar los resultados.
    """
class Vista:
    #se crean los widget de la ventana de tkinter
    def __init__(self):
        self.puente=None
        self.miFormulario=Ventana.Tk()
        self.miFormulario.title("Formulario Registro Cliente")
        #self.auxNombre=Ventana.StringVar()

        self.LabelNombre=Ventana.Label(self.miFormulario, text="Nombre del Cliente: ")
        self.LabelNombre.pack()
        self.LabelApellido=Ventana.Label(self.miFormulario, text="Apellidos del Cliente: ")
        self.LabelApellido.pack()
       
        self.EntryNombre=Ventana.Entry(self.miFormulario)
        self.EntryNombre.pack()
        self.EntryApellido=Ventana.Entry(self.miFormulario)
        self.EntryApellido.pack()
        
        self.BotonEnviar=Ventana.Button(self.miFormulario, text="Enviar", command=self.EnviarDatos)
        self.BotonEnviar.pack()
        
# *********** Zona de metodos de la clase ************************    
    # Metodo que recolecta los datos establecidos por los entry del formulario
    def TomarDatos(self):        
        auxNombre=self.EntryNombre.get()
        auxApellido=self.EntryApellido.get()
        auxLista=[auxNombre,auxApellido]#se crea una variable de estructura de datos tipo lista
        return auxLista
    
    def EnviarDatos(self):
        auxEnviar=self.TomarDatos()#se recibe y se hace el almacenamiento de la estructura de datos
        ## establece una referencia bidireccional entre el controlador y la vista,
        #permitiendo una comunicación eficiente entre los componentes del patrón MVC.
        self.puente.GuardarDatos(auxEnviar)# se envia la estructura de datos al patron Controlador usando la variable puente (referencia bidireccional)
        
        
    def MostrarInfo(self,datoAux):
        self.LabelResult=Ventana.Label(self.miFormulario,text=datoAux)
        self.LabelResult.pack()
                
