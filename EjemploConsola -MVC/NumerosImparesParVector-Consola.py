
# Inicio Clase Patron de Vista
class Vista:
    def __init__(self,DatoControlador):
        self.numeroDato=None
        self.objControlador=DatoControlador
        self.TomarDato()
        
    def TomarDato(self):
        print("digite un Numero entero")
        self.numeroDato=input()
        print("se visualiza desde la vista",self.numeroDato)
        self.objControlador.Calcular(self.numeroDato)
        
        
        
    

# fin Clase Patron Modelo de Vista

# Inicio Clase Controlador
class Controlador:
    def __init__(self,DatoModelo):
        self.objModelo=DatoModelo
        
        
    def Calcular(self,datoAux):
        if int(datoAux)%2==0:
            #auxPar=datoAux
            self.objModelo.listaPar(datoAux)
        else:
            self.objModelo.listaImpar(datoAux)
        
# Fin Clase Patron Controlador
# Inicio Clase Patron Modelo

class Modelo:
    def __init__(self):
        self.ListaPar=[]
        self.ListaImpar=[]
        
        
    def listaPar(self,auxPar):
        self.ListaPar.append(auxPar)
        print("se imprime la lista PAR",self.ListaPar)
        
    def listaImpar(self,auxImpar):
        self.ListaImpar.append(auxImpar)
        print("se imprime la lista IMPAR",self.ListaImpar)
        

# Fin Clase Patron Modelo
# Inicio Clase Menu
print("digite la cantidad de numeros para analizar: ")
aux=int(input())
objModelo=Modelo()
objControlador=Controlador(objModelo)
for i in range(aux):
    objVista=Vista(objControlador)
    
 