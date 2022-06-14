################
# Valentin Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import es_par

"""
En este programa se definen cuatro funciones para testear la funcin es_par()
en caso de introducir numeros pares o impares, negativos o positivos.
"""

def test_es_par_par():
    """
    Caso de prueba de la función es_par() para numeros pares
    """
    numero = 18
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "El numero ingresado es par, se esperaba True"

def test_es_par_impar():
    """
    Caso de prueba de la función es_par() para numeros impares
    """
    numero = 13
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "El numero ingresado es impar, se esperaba False"

def test_es_par_negativo_par():
    """
    Caso de prueba de la función es_par() para numeros negativos pares
    """
    numero = -22
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "El numero ingresado es par, se esperaba True"

def test_es_par_negativo_impar():
    """
    Caso de prueba de la función es_par() para numeros impares
    """
    numero = -31
    resultado = es_par(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "El numero ingresado es impar, se esperaba False"
