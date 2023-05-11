""" ************************ Implementacion del Patron de diseño de software *********************************************
una de las buenas practicas del MVC es lo siguiente:
    1. Separacion de preocupaciones: es decir tratar de separar la logica del modelo de datos a la logica de la vista y la logica de control de datos.
    cada una de los modulos deben estar separados y cumplir con sus respectivas responsabilidades.
    2. Encapsulamiento: las clases deben estar encapsuladas para poder cambiar o modificar sin afectar ninguna de las pares.
    3. Responsabilidades claras: cada clase o modulo debe tener definidas sus responsabilidades.
    4. Modularidad: Es decir cada una de las partes del codigo debe ser reutilizable sin afectar otras partes del codigo
    
    """



# Inicio Clase Patron de Vista
class Vista:
    def __init__(self,DatoControlador):
        self.numeroDato=None
        self.objControlador=DatoControlador
        self.TomarDato()
        
    def TomarDato(self):
        print("digite un Numero entero")
        self.numeroDato=input()
        self.objControlador.Calcular(self.numeroDato)
        DatosLista=self.objControlador.MostrarListas()
        for i in range(len(DatosLista)):
            if i==0:
                print ("Lista de Numero Impares: ", DatosLista[0])
            else:
                print ("Lista de Numero Pares: ", DatosLista[1])
                
    
# fin Clase Patron Modelo de Vista

# Inicio Clase Controlador
class Controlador:
    def __init__(self,DatoModelo):
        self.objModelo=DatoModelo
        
        
    def Calcular(self,datoAux):
        if int(datoAux)%2==0:
            self.objModelo.NumlistaPar(datoAux)
        else:
            self.objModelo.NumlistaImpar(datoAux)
        
        
            
    def MostrarListas(self):
        ImpListaPar=self.objModelo.EnviaListaPar()
        ImpListaImpar=self.objModelo.EnviaListaImpar()
        return ImpListaImpar,ImpListaPar    
# Fin Clase Patron Controlador
# Inicio Clase Patron Modelo

class Modelo:
    def __init__(self):
        self.ListaPar=[]
        self.ListaImpar=[]
        
        
    def NumlistaPar(self,auxPar):
        self.ListaPar.append(auxPar)
        
    def NumlistaImpar(self,auxImpar):
        self.ListaImpar.append(auxImpar)
        
    def EnviaListaPar(self):
        self.ListaPar
        return self.ListaPar
    
    def EnviaListaImpar(self):
        self.ListaImpar
        return self.ListaImpar
        

# Fin Clase Patron Modelo
# Inicio Clase Menu
print("digite la cantidad de numeros para analizar: ")
aux=int(input())
objModelo=Modelo()
objControlador=Controlador(objModelo)
for i in range(aux):
    objVista=Vista(objControlador)
    
 