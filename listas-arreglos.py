# crear arreglo o lista de cliente
lista_cliente=["nelson", "carlos", "Maria"]
#recorrido con index (numero)
print(lista_cliente)
lista_cliente[2]="Juan"
for i in range(len(lista_cliente)):
    print(f" cliente {i} : {lista_cliente[i]}")
#-----------------------------------------------
#recorrido por el objeto 
for cliente in lista_cliente:
    print(f"el nombre es {cliente}")
    
#menu es un bucle y controlar la variable control
while True:
    opcion=int(input("digite 1 si desea continuar: "))
    if opcion==1:
        print("... menu ...")
        print("1. Agregar información")
        print("2. Modificar información")
        print("3. Borrar información")
        seleccion=int(input("Seleccione una opcion del menu: "))
        match seleccion:
            case 1: 
                nombre=input("digite el nuevo nombre del cliente: ")
                lista_cliente.append(nombre)
                print("agrega info")
                print(lista_cliente)
            case 2: 
                print("modifica info")
            case 3: 
                print("elimina info")
    else:
        print("fin del programa")
        break
    
    
    
    
    