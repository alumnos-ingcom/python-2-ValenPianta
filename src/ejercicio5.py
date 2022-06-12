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
    pila = []
    for c in cadena:
        if c == "[":
            pila.append(c)
        elif c == "]":
            if len(pila) == 0:
                return False
            else:
                pila_top = pila.pop()
                if pila_top != "[":
                    return False
    print(len(pila))
    return not len(pila) 
        
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = input("Ingrese la cadena de texto: ")
    resultado = cadena_balanceada(lista)
    if resultado:
        print("Esta balanceada")
    else:
        print("No está balanceada")
    

if __name__ == "__main__":
    principal()
