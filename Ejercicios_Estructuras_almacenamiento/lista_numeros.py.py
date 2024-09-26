lista_numeros=[]#el array
lista2_numeros=[3,5,3,6]
cant=int(input("digite la cantidad de numeros: "))
for i in range(cant):
    num=int(input("escriba el numero: "))
    lista_numeros.append(num)

print(lista_numeros)
suma=0
for numero in lista_numeros:
    print(numero)
    suma=suma+numero
print(f"total suma: {suma}")

lista_numeros.extend(lista2_numeros)
print(lista_numeros)




