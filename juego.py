import random
numero= random.randint(0,100)
numero2= int(input("Por favor introduzca un número: "))
numero_intentos= 0
while numero != numero2:
    if numero2 < numero:
        print("Demasiado pequeño.")
        numero2= int(input("Por favor escoja otro número: "))
        numero_intentos= numero_intentos + 1
    if numero2 > numero:
        print("Demasiado grande.")
        numero2= int(input("Por favor escoja otro número: "))
        numero_intentos= numero_intentos + 1
if numero2==numero:
    numero_intentos= numero_intentos + 1
    print("Enohorabuena, los números coinciden." , " El número de intentos son: " , numero_intentos)