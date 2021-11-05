import random
numero= random.randint(0,100)
numero2= int(input("Por favor introduzca un número: "))
while numero != numero2:
    if numero2 < numero:
        print("Demasiado pequeño.")
        numero2= int(input("Por favor escoja otro número: "))
    if numero2 > numero:
        print("Demasiado grande.")
        numero2= int(input("Por favor escoja otro número: "))
if numero2==numero:
    print("Enohorabuena, los números coinciden.")