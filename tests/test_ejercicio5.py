################
# Valentin Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5 import cadena_balanceada

"""
En este programa se define la funcion para testear la función cadena_balanceada()
en todos los casos propuestos en la consigna.
"""

def test_cadena_balanceada_caso_uno():
    """
    Primer caso de prueba de la función cadena_balanceada
    """
    cadena = ""
    resultado = cadena_balanceada(cadena)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "El resultado no es correcto, se esperaba True"

def test_cadena_balanceada_caso_dos():
    """
    Segundo caso de prueba de la función cadena_balanceada
    """
    cadena = "[]"
    resultado = cadena_balanceada(cadena)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "El resultado no es correcto, se esperaba True"
    
def test_cadena_balanceada_caso_tres():
    """
    Tercer caso de prueba de la función cadena_balanceada
    """
    cadena = "[][]"
    resultado = cadena_balanceada(cadena)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "El resultado no es correcto, se esperaba True"

def test_cadena_balanceada_caso_cuatro():
    """
    Cuarto caso de prueba de la función cadena_balanceada
    """
    cadena = "[[][]]"
    resultado = cadena_balanceada(cadena)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "El resultado no es correcto, se esperaba True"

def test_cadena_balanceada_caso_cinco():
    """
    Quinto caso de prueba de la función cadena_balanceada
    """
    cadena = "]["
    resultado = cadena_balanceada(cadena)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "El resultado no es correcto, se esperaba False"
    
def test_cadena_balanceada_caso_seis():
    """
    Sexto caso de prueba de la función cadena_balanceada
    """
    cadena = "][]["
    resultado = cadena_balanceada(cadena)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "El resultado no es correcto, se esperaba False"
    
def test_cadena_balanceada_caso_siete():
    """
    Séptimo caso de prueba de la función cadena_balanceada
    """
    cadena = "[]][[]"
    resultado = cadena_balanceada(cadena)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "El resultado no es correcto, se esperaba False"
