################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que permita obtener el n-esimo termino de la
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""

def fibonacci(numero):
    """Esta función recibe un número entero positivo y devuelve
    el numero correspondiente a esa posición en la sucesión de fibonacci"""
    
    primero = 0
    segundo = 1
    suma = 0
    contador = 0
    while contador < numero:
        suma = primero + segundo
        primero = segundo
        segundo = suma
        contador += 1
    return suma

def principal():
    """
    Esta función pide ingresar la posición del numero que se desea obtener de
    la sucesión de fibonacci.
    """
    valor = int(input("Ingrese posición del numero de la sucesion de fibonacci que desea: "))
    resultado = fibonacci(valor)
    print(f"El numero en la posición {valor} es el {resultado}")

if __name__ == "__main__":
    principal()
