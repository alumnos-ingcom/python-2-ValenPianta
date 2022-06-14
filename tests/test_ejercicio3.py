################
# Valentin Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import grado_superposicion

"""
En este programa se definen dos funciones para testear la función grado_superposicion()
en caso de introducir listas con y sin superposición.
"""

def test_grado_superposicion():
    """
    Caso de prueba de la función grado_superposicion() para 4 elementos
    """
    lista = ('H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o')
    otra_lista = ('H', 'o', 'l', 'a')
    resultado = grado_superposicion(lista, otra_lista)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado >= 0, "El resultado debe ser un número positivo"
    assert resultado == 4, "El valor no es correcto, se esperaba 4"

def test_grado_superposicion_cero():
    """
    Caso de prueba de la función grado_superposicion() para cero elementos
    """
    lista = ('M', 'u', 'n', 'd', 'o')
    otra_lista = ('H', 'o', 'l', 'a')
    resultado = grado_superposicion(lista, otra_lista)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado >= 0, "El resultado debe ser un número positivo"
    assert resultado == 0, "El valor no es correcto, se esperaba 0"
