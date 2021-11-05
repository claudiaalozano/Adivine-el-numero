# Adivine-el-numero

Mi dirección de GitHub para el repositorio es: [GitHub](https://github.com/claudiaalozano/Adivine-el-numero.git)
https://github.com/claudiaalozano/Adivine-el-numero.git

He resuelto un juego de adivinar valores entre 0 y 99.
El diagrama de flujo que tengo en nuestro código es el siguiente:

![Diagrama de flujo del juego de adivinar el número](/claudiaalozano/Adivine-el-numero/figma adivine un número.jpg)

´´´import random
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
    print("Enohorabuena, los números coinciden." , " El número de intentos son: " , numero_intentos)```
