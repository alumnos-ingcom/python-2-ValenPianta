################
# Valentin Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import codificar, decodificar

"""
En este programa se definen las funciones para testear las funciones codificar() y
decodificar().
"""

def test_codificar():
    """
    Caso de prueba de la función codificar()
    """
    texto = "hola mundo 987 ZZ"
    posiciones = 13
    resultado = codificar(texto, posiciones)
    assert isinstance(resultado, str), "El resultado debe ser una cadena de texto"
    assert resultado == "ubyn zhaqb 210 CC", "El resultado esperado es 'ubyn zhaqb 210 CC'"

def test_decodificar():
    """
    Caso de prueba de la función decodificar()
    """
    texto = "ubyn zhaqb 210 CC"
    posiciones = 13
    resultado = decodificar(texto, posiciones)
    assert isinstance(resultado, str), "El resultado debe ser una cadena de texto"
    assert resultado == "hola mundo 987 ZZ", "El resultado esperado es 'hola mundo 987 ZZ'"

