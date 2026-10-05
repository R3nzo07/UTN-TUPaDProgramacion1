#ejercicio 1
#Se crea la lista con las 10 notas
notas = [4,5,6,6.6,7.5,8,2,3,10,9]
#Se inician los contadores
suma = 0
nota_mayor = float("-inf")
nota_menor = float("inf")
#Se recorren las notas de la lista
for nota in notas:
    print(nota)
    suma += nota
    #Se actualiza la nota mayor y menor
    if nota > nota_mayor:
        nota_mayor = nota
    if nota < nota_menor:
        nota_menor = nota
        #Se calcula el promedio
promedio = suma / len(notas)
#Se imprime el promedio, nota más baja y más alta
print(f"El promedio de las notas es de {promedio}, la nota más baja es {nota_menor} y la nota más alta es {nota_mayor}.")

#ejercicio 2
#Se inica la lista "productos" vacía
productos = []
#Se ingresan 5 productos
for i in range(1,6):
    producto_ingresado = str(input("Ingrese un producto: "))
    productos.append(producto_ingresado)
#Se ordenan alfabeticamente los productos
productos = sorted(productos)
#Se imprime la lista ordenada
print(f"La lista de productos es: {productos}")
#Se pregunta al usuario que elemento quiere eliminar
producto_eliminar = str(input("¿Qué producto desea eliminar?: "))
#Se verifica que el producto a eliminar exista en la lista
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
else:
    print(f"El producto {producto_eliminar} no se encuentra en la lista")
#Se imprime la lista final
print(f"La lista de productos quedó así: {productos}")

#ejercicio 3
#Se crean las listas
numero_aleatorio = []
lista_num_par = []
lista_num_impar = []
#Se importa un número aleatorio
import random
for i in range(1,16):
    num_random = random.randint(1, 100)
    numero_aleatorio.append(num_random)
#Se verifica si el número es par o impar y se agrega a la respectiva lista
    if num_random % 2 == 0:
        lista_num_par.append(num_random)          
    else:
        lista_num_impar.append(num_random)
#Se imrpime la cantidad de números pares e impares       
print(f"La cantidad de números pares es de {len(lista_num_par)} y la de números impares es de {len(lista_num_impar)}")
 
#ejercicio 4
#Se inica la lista "datos_sin_repetir" vacía
datos_sin_repetir = []
#Se crea la lista de datos ya asignada
datos = [1,3,5,3,7,1,9,5,3]
#Se recorre la lista "datos"
for numero in datos:
#Si el número no está en la lista "datos_sin_repetir", se añade    
    if numero not in datos_sin_repetir:
        datos_sin_repetir.append(numero)
#Se imprime la nueva lista
print(f"La lista sin elementos repetidos queda así: {datos_sin_repetir}")

#ejercicio 5
#Se define la lista de estudiantes
nombres = ["Jenaro","Alejandra","Sebastian","Renzo","Agustin","Francisco","Juan","Pedro"]
#Se consulta al usuario si agrega o elimina un nombre de estudiante de la lista
opcion = str(input("¿Desea agregar un nuevo estudiante o eliminar uno existente? agregar/eliminar: "))
#Si la opción es agregar, se pide el nuevo nombre a la lista
if opcion == "agregar":
    nombre_nuevo = str(input("Escribe el nombre del estudiante a agregar: "))
    nombres.append(nombre_nuevo)
#Si la opción es eliimar, se elimina el nombre de la lista
elif opcion == "eliminar":
    nombre_eliminar = str(input("Escribe el nombre del estudiante a eliminar: "))
    if nombre_eliminar in nombres:
        nombres.remove(nombre_eliminar)
    else:
        print("Ese estudiante no está en la lista")
else:
    print("Opción invalida")
#Se imprime la lista final de los estudiantes
print(f"La lista final de los estudiantes queda así: {nombres}")

#ejercicio 6
#Se define la lista de números
lista_numeros = [1,2,3,4,5,6,7]
#Se guarda el último número 
ultima_posicion = lista_numeros[6]
#Se recorre la lista desde la pos. 6 a la 1 
for posicion in range(6, 0, -1):
    #Se mueve cada número una posición hacia la derecha
    lista_numeros[posicion] = lista_numeros[posicion - 1]
#Se coloca el último número al principio
lista_numeros[0] = ultima_posicion
#Se imprime la lista
print(lista_numeros)

#ejercicio 7
#Se crea la matriz con las temperaturas mínimas y máximas de los 7 días
temperaturas = [
    [10, 20],
    [12, 24],
    [8, 18],
    [15, 27],
    [11, 19],
    [9, 21],
    [13, 25]
]
#Se inicina las variables para acumular las temperaturas y para encontrar la mayor amplitud térmica
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0
#Se recorre la matriz
for dia in range(7):
    #Se suma las temperaturas mínimas
    suma_minimas = suma_minimas + temperaturas[dia][0]
    #Se suma las temperaturas máximas
    suma_maximas = suma_maximas + temperaturas[dia][1]
    #Se calcula la amplitud térmica del día
    amplitud = temperaturas[dia][1] - temperaturas[dia][0]
    #Se verifica si es la mayor amplitud encontrada
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dia + 1
#Se calcula los promedios
promedio_minimas = suma_minimas / 7
promedio_maximas = suma_maximas / 7
#Se imprimeo los resultados
print(f"El promedio de temperaturas mínimas es: {promedio_minimas}")
print(f"El promedio de temperaturas máximas es: {promedio_maximas}")
print(f"El día con mayor amplitud térmica fue el día {dia_mayor_amplitud}")

#ejercicio 8
#Se crea la matriz con las notas de 5 estudiantes en 3 materias
notas = [
    [8, 7, 9],
    [6, 5, 8],
    [10, 9, 10],
    [7, 6, 8],
    [9, 8, 7]
]
#Se calcula el promedio de cada estudiante
for estudiante in range(5):
    suma = 0
#Se suma las 3 notas del estudiante
    for materia in range(3):
        suma = suma + notas[estudiante][materia]
    promedio = suma / 3
    print(f"El promedio del estudiante {estudiante + 1} es: {promedio}")
print()
#Promedio de cada materia
for materia in range(3):
    suma = 0
#Se suma las notas de los 5 estudiantes para calcular el promedio
    for estudiante in range(5):
        suma = suma + notas[estudiante][materia]
    promedio = suma / 5
    print(f"El promedio de la materia {materia + 1} es: {promedio}")

#ejercicio 9
#Se crea la matriz 3x3 que representa el tablero
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

#Se realizan 9 jugadas como máximo
for turno in range(9):
#Se determinar el jugador según el turno
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"
#Se imprime el turno del jugador correspondiente
    print(f"Turno del jugador {jugador}")

#Se pide la fila y la columna
    fila = int(input("Ingrese la fila (0, 1 o 2): "))
    columna = int(input("Ingrese la columna (0, 1 o 2): "))

#Se coloca la ficha si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("La casilla ya está ocupada.")

#Se muestra el tablero
    for fila in tablero:
        print(fila)

    print()

#ejercicio 10
#Se crea la matriz 4x7 que representa 4 productos y 7 días
ventas = [
    [10, 5, 8, 6, 7, 9, 4],   
    [3, 7, 2, 5, 6, 4, 8],    
    [9, 6, 7, 8, 5, 3, 2],    
    [4, 8, 6, 7, 9, 5, 3]     
]
#Se calcula el total vendido por producto
for producto in range(4):
    total_producto = 0
    for dia in range(7):
        total_producto = total_producto + ventas[producto][dia]
#Se imprime el total vendido del producto
    print(f"El total vendido del producto {producto + 1} es de: {total_producto}")
print()
#Se inicia el contador del día con mayores ventas totales
mayor_ventas_dia = 0
dia_mayor_ventas = 0
#Se calcula el día con mayores ventas
for dia in range(7):
    total_dia = 0
    for producto in range(4):
        total_dia = total_dia + ventas[producto][dia]
    if total_dia > mayor_ventas_dia:
        mayor_ventas_dia = total_dia
        dia_mayor_ventas = dia + 1
print(f"El día con mayores ventas fue el día {dia_mayor_ventas}")
print()
#Se inicia el contador del producto más vendido en la semana
mayor_total_producto = 0
producto_mas_vendido = 0
#Se calcula el roducto más vendido en la semana
for producto in range(4):
    total_producto = 0
    for dia in range(7):
        total_producto = total_producto + ventas[producto][dia]
    if total_producto > mayor_total_producto:
        mayor_total_producto = total_producto
        producto_mas_vendido = producto + 1
print(f"El producto más vendido en la semana fue el producto {producto_mas_vendido}")