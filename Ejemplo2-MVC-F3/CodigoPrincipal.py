from ClaseModelo import Cliente
from ClaseVista import Vista
from ClaseControlador import Controlador

#********* Clase que ejecuta el codigo General.........*************************
class CodigoPrincipal:
    def __init__(self):
        ObjVista=Vista()
        ObjModelo=Cliente()
        
        Controlador(ObjVista,ObjModelo)
        ObjVista.miFormulario.mainloop()
                
# ****************** Codigo Main del Programa *********************
main=CodigoPrincipal()
    



