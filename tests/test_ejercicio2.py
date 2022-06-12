################
# Valentin Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import max_min_prom

"""
En este programa se definen dos funciones para testear la funcin max_min_prom()
en caso de introducir numeros positivos y negativos.
"""

def test_max_min_prom_positivos():
    """
    Caso de prueba de la función max_min_prom() para numeros positivos
    """
    secuencia = [2, 3, 6, 10]
    resultado = max_min_prom(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado[0] == 10, "El valor máximo no es correcto, se esperaba 10"
    assert resultado[1] == 2, "El valor mínimo no es correcto, se esperaba 2"
    assert resultado[2] == 5.25, "El valor promedio no es correcto, se esperaba 5.25"

def test_max_min_prom_negativos():
    """
    Caso de prueba de la función max_min_prom() para numeros negativos
    """
    secuencia = [-2, -5, -1]
    resultado = max_min_prom(secuencia)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado[0] == -1, "El valor máximo no es correcto, se esperaba -1"
    assert resultado[1] == -5, "El valor mínimo no es correcto, se esperaba -5"
    assert resultado[2] == -2.6666666666666665, "El valor promedio no es correcto, se esperaba -2.6666666666666665"
