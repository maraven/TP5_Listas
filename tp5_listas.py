import random
'''
#Ejercicio 1 Lista de notas de estudiantes.
print(f"--- EJERCICIO 1 ---")
Notas = [6,5,10,3,2,4,9,1,8,7]
sum = 0
print(f"Lista de notas de estudiantes:")
for i in range(len(Notas)): #se utiliza funcion len para obtener la cantidad de elementos de la lista
    print(f"Estudiante {i+1}: {Notas[i]}")
    sum += Notas[i] #se va sumando cada nota a la variable sum

#calculo de promedio
promedio = sum / len(Notas) #se divide la suma total de las notas por la cantidad de estudiantes
print(f"Promedio de notas: {promedio}")

#Nota mas alta y baja
Notas.sort() #se ordena la lista de notas de menor a mayor
print(f"Nota más baja: {Notas[0]}") #la nota más baja es el primer elemento de la lista ordenada
print(f"Nota más alta: {Notas[-1]}") #la nota más alta es el último elemento de la lista ordenada

#Ejercicio 2 Se pide al usuario que cargue 5 productos en una lista.
print(f"--- EJERCICIO 2 ---")
ListaProductos = []
for i in range(5):
    Producto = input(f"Ingrese producto {i+1}: ").strip()
    #validacion 
    while not Producto.isalpha():
        print(f"Error. Dato no válido")
        Producto = input(f"Ingrese producto {i+1}: ").strip()
    ListaProductos.append(Producto) #se agrega el producto a la lista utilizando el metodo append()

#se crea nueva lista ordenada con sorted() y se muestra
Productos_ordenados = sorted(ListaProductos)
for i in range(len(Productos_ordenados)):
    print(f"Producto {i+1}: {Productos_ordenados[i]}")

#eliminacion y actualizacion de la lista original con el metoro remove()
eliminar= input(f"Ingrese el producto a eliminar: ").strip()
#validacion y eliminacion del producto
while not eliminar in Productos_ordenados:
    print(f"Error. Producto no encontrado.")
    eliminar= input(f"Ingrese el producto a eliminar: ").strip()

Productos_ordenados.remove(eliminar)
print(f"Producto {eliminar} eliminado.")
#actualizacion de la lista original
print(f"Lista actualizada de productos:")
for i in range(len(Productos_ordenados)):
    print(f"Producto {i+1}: {Productos_ordenados[i]}")


#Ejercicio 3 Generar una lista con 15 números enteros al azar entre 1 y 100.
print(f"--- EJERCICIO 3 ---")
random_list = []
list_par = []
list_impar = []
for i in range(15):
    num = random.randint(1, 100) #se genera un numero aleatorio utilizando la funcion randint() del modulo random
    random_list.append(num) #se agrega el numero a la lista utilizando el metodo append()

#a partir de la lista generada se crean 2 listas para pares e impares
for i in range(len(random_list)):   
    if random_list[i] % 2 == 0:
        list_par.append(random_list[i])  
    else:
        list_impar.append(random_list[i])

#se muestran la listas pares e impares
print(f"Lista de numeros pares:") 
for i in range(len(list_par)):
    print(f"Número par {i+1}: {list_par[i]}")
print(f"Lista de numeros impares:")
for i in range(len(list_impar)):
    print(f"Número impar {i+1}: {list_impar[i]}")


#Ejercicio 4 Lista de valores repetidos
print(f"--- EJERCICIO 4 ---")
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista = []
#Recorre la lista datos y agrega la variable a una nueva lista si no esta repetida
for i in datos:
    if i not in lista:
        lista.append(i)
#Se imprimen la lista original y la lista sin repetidos.
print("Original:", datos)
print("Sin repetidos:", lista)


#Ejercicio 5 Crear una lista con los nombres de 8 estudiantes presentes en clase.
print(f"--- EJERCICIO 5 ---")
#Lista de estudiantes 
estudiantes = ["Ariel", "Julian", "Enzo", "Diego", "Gonzalo", "Lionel", "Rodrigo", "Emi"]

print("Lista inicial de estudiantes:")
for i in estudiantes:
    print(f"- {i}")

#Se agrega o elimina estudiante y validacion del dato. 
while True:
    accion = input("\n¿Desea agregar (A) o eliminar (E) un estudiante? (A/E): ").upper()
    if accion in ["A", "E"]:
        break
    print("Error: Ingrese 'A' para agregar o 'E' para eliminar.")

if accion == "A":
    #Agregar estudiante con .append con el dato validado
    while True:
        nuevo = input("Ingrese el nombre del nuevo estudiante: ").capitalize()
        if nuevo.isalpha():
            estudiantes.append(nuevo)
            print(f"{nuevo} ha sido agregado.")
            break
        print("Error: El nombre debe contener solo letras.")

elif accion == "E":
    #Eliminar estudiante con .remove 
    while True:
        #se utiliza el metodo .capitalize() para no tener problemas en la comparacion y eliminacion del estudiante de la lista.
        eliminar = input("Ingrese el nombre del estudiante a eliminar: ").capitalize()
        #se valida el dato con isalpha() y se verifica que tambien este en la lista.
        if eliminar.isalpha():
            if eliminar in estudiantes:
                estudiantes.remove(eliminar)
                print(f"{eliminar} ha sido eliminado.")
                break
            else:
                print(f"El estudiante '{eliminar}' no se encuentra en la lista.")
                # Damos la opción de salir si no lo encuentra para evitar bucle infinito
                if input("¿Desea intentar con otro nombre? (S/N): ").upper() == "N":
                    break
        else:
            print("Error: El nombre debe contener solo letras.")

#Lista actualizada
print("\n--- Lista Final de Estudiantes ---")
for estudiante in estudiantes:
    print(estudiante)

'''

