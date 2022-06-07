################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne True cuando un número entero
es par y False cuando no lo sea, sin utilizar módulo. (%)
"""

def es_par(numero):
    """Esta función recibe un numero entero y retorna True en caso de que sea
    par y False cuando no lo es."""
    return numero / 2 == numero // 2

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese número: "))
    if es_par(numero):
        print("Es par!")
    else:
        print("No es par")


if __name__ == "__main__":
    principal()