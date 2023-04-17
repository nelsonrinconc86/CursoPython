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