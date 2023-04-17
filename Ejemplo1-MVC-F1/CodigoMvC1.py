import tkinter as Ventana

#********* Clase del Patron Vista.........*************************
:pencil2: 
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
                
#********* Clase del Patron Controlador.........*************************        
"""
Crear una clase Controlador que actúe como intermediario entre el modelo y la vista.
Esta clase deberá tener métodos para recibir la entrada del usuario desde la vista,
llamar a los métodos correspondientes en el modelo y actualizar la vista con los resultados.
"""
class Controlador:
    def __init__(self,DatoObjVista,DatoObjModelo):
        print(" se ejecuta la clase controladora")
        self.ObjModelo=DatoObjModelo
        self.ObjVista=DatoObjVista
        self.ObjVista.puente=self# establece una referencia bidireccional entre el controlador y la vista,
        #permitiendo una comunicación eficiente entre los componentes del patrón MVC.
                
    def GuardarDatos(self,DatoAux):#se recibe los datos del patron Controlador
        self.ObjModelo.ActualizarBD(DatoAux)#se envia los datos al patron Modelo
        self.ImprimirDatos()
    
    def ImprimirDatos(self):
        auxImprimir=self.ObjModelo.ImprimirBd()
        self.ObjVista.MostrarInfo(auxImprimir)
        print("muestra desde el controlador ",auxImprimir)
        
#****************** codigo de Patorn Modelo *****************************************
        """
        Crear una clase Modelo que contenga los datos y los métodos necesarios para manipular los datos. En este caso,
        la clase Cliente ya está haciendo el trabajo de Modelo, pero se deben hacer algunos ajustes para que se ajuste
        al patrón. La clase Cliente debe contener métodos para agregar, actualizar, eliminar y buscar datos.
        También debe haber una forma de acceder a los datos almacenados, como una lista o un diccionario.
        
        """
class Cliente:
    def __init__(self):
        self.listaClientes=[["Nelson","Rinconc"]]
        self.BdNombre=None
        self.bdApellido=None
        
        
        
    def ActualizarBD(self,DatoClienteNombre):#se recibe los datos de la estructura de datos del controlador
        AuxLista=DatoClienteNombre#se almacena los datos en una lista auxiliar para poder anexar a la lista original de base de datos
        self.listaClientes.append(AuxLista) # se agrega la lista auxiliar a la lista original de la base de datos.
        print("Datos Guardador exitosamente") 
        
    def ImprimirBd(self):
        aux=self.listaClientes
        return aux
        
        
            
        
#********* Clase que ejecuta el codigo General.........*************************
class CodigoPrincipal:
    def __init__(self):
        ObjVista=Vista()
        ObjModelo=Cliente()
        
        Controlador(ObjVista,ObjModelo)
        ObjVista.miFormulario.mainloop()
                
# ****************** Codigo Main del Programa *********************
main=CodigoPrincipal()
    



