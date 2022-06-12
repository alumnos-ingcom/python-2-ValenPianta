################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que determine
si una cadena con corchetes está balanceada.
"""

def cadena_balanceada(cadena):
    """Esta función recibe una cadena de texto y devuelve un valor True
    si cada corchete que abre tiene su par que cierra, y false si no es así
    """
    corchete_abierto = 0
    corchete_cerrado = 0
    lista = []
    contador = 0
    for i in cadena:
        if cadena[contador] == "[":
            corchete_abierto += 1
            lista.append(i)
            contador += 1
        elif cadena[contador] == "]":
            corchete_cerrado += 1
            lista.append(i)
            contador += 1
        else:
            contador += 1
    if corchete_abierto == corchete_cerrado:
        contador = 0
        for c in lista:
            if lista[contador] == "[":
                contador += 1
                return True
            elif lista[contador] == "]":
                contador += 1
                return False
        return lista
    else:
        return False  
        
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = "[]][[]]"
    resultado = cadena_balanceada(lista)
    print(resultado)
    

if __name__ == "__main__":
    principal()
