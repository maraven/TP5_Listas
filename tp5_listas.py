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


#Ejercicio 6 Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
#(el último pasa a ser el primero).
print(f"--- EJERCICIO 6 ---")
lista = [10, 20, 30, 40, 50, 60, 70]

# Rotar todos los elementos una posición hacia la derecha 
# El último [-1] pasa al inicio, seguido de todo lo demás [:-1]
rotacion = [lista[-1]] + lista[:-1]

print("Lista Original:")
# Usamos len() para obtener el índice y mostrarlo correctamente
for i in range(len(lista)):
    print(f"Posición {i}: {lista[i]}")

print("\nLista Rotada:")
for i in range(len(rotacion)):
    print(f"Posición {i}: {rotacion[i]}")


#Ejercicio 7 Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#--Calcular el promedio de las mínimas y el de las máximas.
#--Mostrar en qué día se registró la mayor amplitud térmica.
print(f"--- EJERCICIO 7 ---")
matriz_temperaturas = [] 
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
#Se crea la matriz
for i in range(7):
    print(f"Datos para el día {dias[i]}:")
    
    #Validacion de temp mínima.
    while True:
        min_ingresada = input("  Ingrese temperatura mínima: ")
        #Se usa .lstrip() por si ingresan temperaturas bajo cero
        if min_ingresada.lstrip('-').isdigit():
            t_min = int(min_ingresada)
            break
        print("Error: Ingrese un número entero válido.")

    #Validacion temp máxima
    while True:
        max_ingresada = input("  Ingrese temperatura máxima: ")
        if max_ingresada.lstrip('-').isdigit():
            t_max = int(max_ingresada)
            #Se verifica que la temp. máxima no sea menor a la mínima
            if t_max >= t_min:
                break
            else:
                print(f"Error: La máxima no puede ser menor a la mínima ({t_min}).")
        else:
            print("Error: Ingrese un número entero válido.")
    
    #Se agregan temperaturas como matriz con .append()
    matriz_temperaturas.append([t_min, t_max])

#Calculos, se inician sumadores
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor_amplitud = ""

for i in range(len(matriz_temperaturas)):
    min_actual = matriz_temperaturas[i][0]
    max_actual = matriz_temperaturas[i][1]
    
    suma_minimas += min_actual
    suma_maximas += max_actual
    
    #Amplitud térmica = Máxima - Mínima
    amplitud = max_actual - min_actual
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]

print("\n--- RESULTADOS DE LA SEMANA ---")
print(f"Promedio de temperaturas mínimas: {suma_minimas / 7:.2f}°C")
print(f"Promedio de temperaturas máximas: {suma_maximas / 7:.2f}°C")
print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C el día {dia_mayor_amplitud}.")


#Ejercicio 8 Crear una matriz con las notas de 5 estudiantes en 3 materias.
#Mostrar el promedio de cada estudiante.
#Mostrar el promedio de cada materia.
print(f"--- EJERCICIO 8 ---")
m_notas = []
cant_estudiantes = 5
cant_materias = 3
#Se carga la matriz con el metodo .append(), se declara estudiantes como fila y materias como columnas.
for i in range(cant_estudiantes):
    notas_estudiante = []
    print(f"\nCarga de notas para el Estudiante {i + 1}:")
    for j in range(cant_materias):
        #validacion con isdigit() y se verifica que sea de 0 a 10 la nota
        while True:
            entrada = input(f"Ingrese nota de Materia {j + 1}: ")
            if entrada.isdigit():
                nota = int(entrada)
                if 0 <= nota <= 10:
                    notas_estudiante.append(nota)
                    break
                else:
                    print("Error: La nota debe estar entre 0 y 10.")
            else:
                print("Error: Ingrese un número entero válido.")
    
    m_notas.append(notas_estudiante)

#Promedio por estudiante
print("\n--- PROMEDIO POR ESTUDIANTE ---")
for i in range(cant_estudiantes):
    suma_notas = 0 #Se resetea sumador para cada estudiante
    for j in range(cant_materias):
        suma_notas += m_notas[i][j]
    
    promedio = suma_notas / cant_materias
    print(f"Estudiante {i + 1}: Promedio = {promedio:.2f}")

#Promedio por materia, se recorre la matriz por columnas
print("\n--- PROMEDIO POR MATERIA ---")
for j in range(cant_materias):
    suma_materia = 0 #Se resetea sumador para cada materia
    for i in range(cant_estudiantes):
        suma_materia += m_notas[i][j]
    
    promedio_m = suma_materia / cant_estudiantes
    print(f"Materia {j + 1}: Promedio General = {promedio_m:.2f}")


#Ejercicio 9 Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#Inicializarlo con guiones "-" representando casillas vacías.
#Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#Mostrar el tablero después de cada jugada.
print(f"--- EJERCICIO 9 ---")
#Se inicializa con guiones para las casillas vacias.
tateti = []
for i in range(3):
    fila= ["-", "-", "-"] 
    tateti.append(fila)

#se define funcion de tablero para no repetir codigo
def tablero():
    print(f"\n  1 2 3")
    for i in range(3):
        print(f"{i+1}", end=" ") #se utiliza end="" para que quede uno al lado del otro
        for j in range(3):
            print(tateti[i][j], end=" ")
        print() #Salto de linea.

turno = 0 
jugadores = ["X", "O"]
ganador= False

#JUEGO
while turno < 9 and not ganador: #Finaliza el juego cuando se hace ta-te-ti o cuando se ocupan todos los espacios
    
    tablero()
    
    simbolo= jugadores[turno % 2] #se utiliza modulo para alternar los turnos del jugador por medio del indice.
    print(f"Turno jugador: '{simbolo}'")

    #Ingreso de simbolos y validacion utilizando posiciones/coordenadas.
    while True:
        pos_f = input(f"Ingrese fila (1-3): ").strip()
        pos_c = input(f"Ingrese columna (1-3): ").strip()
        if pos_f.isdigit() and pos_c.isdigit():
            f= int (pos_f)
            c= int (pos_c)
            if (1 <= f <= 3) and (1 <= c <= 3):
                if tateti[f-1][c-1] == "-": #-1 debido que los indices comienzan en 0
                    tateti[f-1][c-1]= simbolo
                    break
                else:
                    print(f"Error, Casilla ocupada.")
            else:
                print(f"Error de posicion, debe ser 1, 2 o 3.")
        else:
            print(f"Error. Dato no válido.")

    #Se verifica si hay ta-te-ti y se finaliza el juego con bandera.
    
    #TA-TE-TI por filas
    for i in range(3):
        sum=0
        for j in range(3):
            if tateti[i][j] == simbolo:
                sum += 1
        if sum == 3:
            ganador= True
    
    #TA-TE-TI por columnas 
    for j in range(3):
        sum_c = 0
        for i in range(3):
            if tateti[i][j] == simbolo:
                sum_c += 1
        if sum_c == 3:
            ganador = True
    
    #TA-TE-TI por diagonales
    diag1= 0
    diag2= 0
    for i in range(3):
        if tateti[i][i] == simbolo: #se verifica la diagonal (0,0) (1,1) (2,2)
            diag1 += 1
        if tateti[i][2 - i] == simbolo: #se verifica la segunda diagonal (0,2)(1,1)(2,0)
            diag2 += 1
    if diag1 == 3 or diag2 == 3:
        ganador= True

    turno += 1

print("---JUEGO FINALIZADO---")
tablero()
'''
