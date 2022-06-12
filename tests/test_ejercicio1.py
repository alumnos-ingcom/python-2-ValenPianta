################
# Valentin Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import es_par

"""
En este programa se definen dos funciones para testear la funcin es_par()
en caso de introducir numeros pares e impares.
"""

def test_es_par_par():
    """
    Caso de prueba de la función es_par() para numeros pares
    """
    numero = 18
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado == True, "El numero ingresado es par, se esperaba True"

def test_es_par_impar():
    """
    Caso de prueba de la función es_par() para numeros impares
    """
    numero = 13
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado == False, "El numero ingresado es par, se esperaba True"
