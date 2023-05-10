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
    