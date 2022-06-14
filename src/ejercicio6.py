################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una funcion que codifique un texto rotandolo
una cantidad de posiciones ajustable.

Implementar la funcion que decodifique el texto rotado
una cantidad de posiciones ajustable.
"""

def codificar(texto, posiciones):
    """Esta función recibe una cadena de texto y la cantidad de posiciones a rotar,
    y devuelve la misma cadena de texto encriptada segun el cifrado de cesar"""
    conversion = 0
    codificado = ""
    diferencia = 0
    for c in texto:
        conversion = ord(c)
        if conversion >= 48 and conversion <= 57:
            while posiciones > 10:
                posiciones -= 10
            conversion += posiciones
            if conversion > 57:
                diferencia = conversion - 57
                conversion = 48
                conversion += diferencia - 1
        elif conversion >= 97 and conversion <= 122:
            while posiciones > 26:
                posiciones -= 26
            conversion += posiciones
            if conversion > 122:
                diferencia = conversion - 122
                conversion = 97
                conversion += diferencia - 1
        elif conversion >= 65 and conversion <= 90:
            while posiciones > 26:
                posiciones -= 26
            conversion += posiciones
            if conversion > 90 and conversion <= 122:
                diferencia = conversion  - 90
                conversion = 65
                conversion += diferencia - 1
        codificado += chr(conversion)
    return codificado

def decodificar(texto, posiciones):
    """Esta función recibe una cadena de texto codificada segun el cifrado de
    cesar y la cantidad de posiciones a rotar, y devuelve la misma cadena de texto decodificado"""
    conversion = 0
    codificado = ""
    for c in texto:
        conversion = ord(c)
        if conversion >= 48 and conversion <= 57:
            while posiciones > 10:
                posiciones -= 10
            conversion -= posiciones
            if conversion < 48:
                diferencia = 48 - conversion
                conversion = 57
                conversion -= diferencia - 1
            
        elif conversion >= 97 and conversion <= 122:
            while posiciones > 26:
                posiciones -= 26
            conversion -= posiciones
            if conversion < 97:
                diferencia = 97 - conversion
                conversion = 122
                conversion -= diferencia - 1
            
        elif conversion >= 65 and conversion <= 90:
            while posiciones > 26:
                posiciones -= 26
            conversion -= posiciones
            if conversion < 65:
                diferencia = 65 - conversion
                conversion = 90
                conversion -= diferencia - 1
        codificado += chr(conversion)
    return codificado

def principal():
    """
    Esta función pide por consola ingresar el texto a codificar y la cantidad de posiciones
    que desea rotar. Luego muestra el texto codificado, y la decodificación a partir del
    texto codificado.
    
    """
    texto = input("Ingrese texto a codificar: ")
    posiciones = int(input("Ingrese cantidad de posiciones a rotar: "))
    codificado = codificar(texto, posiciones)
    print(f"El texto codificado es: {codificado}")
    decodificado = decodificar(codificado, posiciones)
    print(f"El texto decodificado es: {decodificado}")

if __name__ == "__main__":
    principal()
