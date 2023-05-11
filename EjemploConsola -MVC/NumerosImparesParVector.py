import tkinter as Ventana

#************* Inicio Clase Patron Modelo de Vista *********************************
class Vista:
    def __init__(self,DatoControlador):
        self.objControlar=DatoControlador
        formulario=Ventana.Tk()
        formulario.title("Numeros Enteros")
        
        marco1=Ventana.LabelFrame(formulario, text="Toma de datos")
        marco1.config(background="pink")
        marco1.pack()
        
        Texto1Label=Ventana.Label(marco1, text="Digite un numero entero: ")
        Texto1Label.config(background="pink")
        Texto1Label.pack()
        
        self.Entry1=Ventana.Entry(marco1)
        self.Entry1.pack()
        botonEnviar=Ventana.Button(marco1, text="Enviar Datos", command=self.TomaDatos)
        botonEnviar.pack()
        #botonEnviar.grid(column=0,row=0)        
        botonImprimir=Ventana.Button(marco1, text="Imprimir Datos", command=self.ImprimirDatos)
        botonImprimir.pack()
        #botonImprimir.grid(column=1,row=0)
        
        
        formulario.mainloop()
    
    def TomaDatos(self):
        DatoNumero=self.Entry1.get()
        #print("impreso desde el patron vista", DatoNumero)
        self.objControlar.EnviarDatosNumeros(int(DatoNumero))
        
    def ImprimirDatos(self):
        ListarPar=self.objControlar.MostrarListasPar()
        print("la Lista de Numeros de Pares: ", ListarPar)
        listaImpar=self.objControlar.MostrarListasImpar()
        print("la Lista de Numeros de ImPares: ", listaImpar)
        
#************* Fin Clase Patron Modelo de Vista *********************************
#************* Inicio Clase Patron Controlador **********************************
class Controlador:
    def __init__(self,DatoModelo):
        self.objModelo=DatoModelo
                
    def EnviarDatosNumeros(self,DatosNumeros):
        #print("impreso desde el controlador", DatosNumeros)
        if DatosNumeros%2==0:
            self.objModelo.ResibirNumPar(DatosNumeros)
        else:
            self.objModelo.ResibirNumImpar(DatosNumeros)
        
    def MostrarListasPar(self):
        ListasPar=self.objModelo.EnviarListaNumPar()
        return ListasPar
    def MostrarListasImpar(self):
        ListaImpar=self.objModelo.EnviarListaNumImpar()
        return ListaImpar
        
        
#************* fin Clase Patron Controlador **********************************
#************* Inicio Clase Patron Modelo **********************************
class Modelo:
    def __init__(self):
        self.ListaPar=[]
        self.ListaImpar=[]
        
        
    def ResibirNumPar(self,NumeroDato):
        self.ListaPar.append(NumeroDato)
        #print("Dato Guardado en la base de datos", self.ListaPar)
        
    def ResibirNumImpar(self,NumeroDato):
        self.ListaImpar.append(NumeroDato)
        #print("Dato Guardado en la base de datos", self.ListaImpar)
        
    def EnviarListaNumPar(self):
        return self.ListaPar
        
    def EnviarListaNumImpar(self):
        return self.ListaImpar
    

        
#************* fin Clase Patron Modelo **********************************


        
#************* Inicio Clase Menu *********************************        
class Menu:
    def __init__(self):
        objModelo=Modelo()
        objControlador=Controlador(objModelo)
        objVista=Vista(objControlador)
        
        
        
        

        

objMenu=Menu()