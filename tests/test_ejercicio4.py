################
# Valentin Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import fibonacci

"""
En este programa se define la funcion para testear la función fibonacci().
"""

def test_fibonacci():
    """
    Caso de prueba de la función fibonacci()
    """
    numero = 6
    resultado = fibonacci(numero)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado >= 0, "El resultado debe ser un número positivo"
    assert resultado == 13, "El valor no es correcto, se esperaba 4"
