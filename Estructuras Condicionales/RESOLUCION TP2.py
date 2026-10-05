#ejercicio 1
#Ingreso de edad
edad = int(input("Ingrese su edad: "))
#Comprobación de mayoría de edad
if edad >= 18:
    print("Es mayor de edad")

#ejercicio 2
#Se solicita nota al usuario
nota = int(input("Ingrese su nota: "))
#Comprobación de que su nota está aprobada o desaprobada
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#ejercicio 3
#Se socilita al usuario un número
numero_usuario = int(input("Ingrese un número: "))
#Se comprueba si el número ingresado es par o impar
if numero_usuario % 2 == 0:
    print("Ha ingresado un número par")
elif numero_usuario != 0:
    print("Por favor, ingrese un número par")

#ejercicio 4
#Se solicita al usuario que ingrese su edad
edad_usuario = int(input("Ingrese su edad: "))
#Se comprueba si el usuario es niño/a, adolescente, adulto/a joven o adulto/a
if edad_usuario < 12:
    print("Niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Adolescente")
elif edad_usuario >= 18 and edad_usuario < 30: 
    print("Adulto/a joven")
else:
    print("Adulto/a")

#ejercicio 5
#Se solicita al usuario el ingreso de una contraseña
contrasena = input("Ingrese una contraseña: ")
#Se comprueba que la contraseña contenga entre 8 a 12 caracteres
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6
# Importa el módulo para generar números aleatorios
import random 
# Genera una lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Importa las funciones estadísticas necesarias
from statistics import mode, median, mean
# Calcula la moda, mediana y media de la lista
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
# Muestra los valores calculados
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
# Compara las medidas estadísticas para determinar el tipo de sesgo
if media > mediana > moda:
    print("El sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("El sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

#ejercicio 7
# Solicita al usuario una palabra o frase
palabra_frase = input("Ingrese una palabra o frase:")
# Obtiene la última letra y la convierte a minúscula
ultima_letra = palabra_frase[-1].lower()
# Verifica si la última letra es una vocal
if ultima_letra in "aeiou":
    print(f"{palabra_frase}!")
else:
    print(f"{palabra_frase}")

#ejercicio 8
#Solicita al usuario su nombre
nombre = input("Ingrese su nombre:")
#Solicita al usuario la opción que desee
opcion = int(input("Ingrese la opción que desee: 1- Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2- Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3- Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."))
#Convierte el nombre dependiendo la opción solicitada
if opcion == 1:
    print(f"{nombre.upper()}")
elif opcion == 2:
    print(f"{nombre.lower()}")
elif opcion == 3:
    print(f"{nombre.title()}")

#ejercicio 9
#Solicita al usuario una magnitud de un terremoto
magnitud = float(input("Ingrese la magnitud de un terremoto"))
#Clasifica la magnitud en la escala de Ritcher
if magnitud < 3: 
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else: 
    print("Extremo (puede causar graves daños a gran escala")

#ejercicio 10
#Solicita al usuario ingresar un hemisferio
hemisferio = input("Ingrese en qué hemisferio se encuentra (N/S):").upper()
#Solicita al usuario ingresar un mes
mes = int(input("Ingrese número del mes que es:"))
#Solicita al usuario ingresar un día
dia = int(input("Ingrese número del día que es:"))
#Si es hemisferio N se clasifica de esta manera
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        print("Se encuentra en Invierno")
    elif (mes == 3 and dia >= 21 ) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en Primavera")
    elif (mes == 6 and dia >= 21 ) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        print("Se encuentra en Verano")
    elif (mes == 9 and dia >= 21 ) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        print("Se encuentra en Otoño")
#Si es hemisferio S se clasifica de esta manera        
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        print("Se encuentra en Verano")
    elif (mes == 3 and dia >= 21 ) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en Otoño")
    elif (mes == 6 and dia >= 21 ) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        print("Se encuentra en Invierno")
    elif (mes == 9 and dia >= 21 ) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        print("Se encuentra en Primavera")