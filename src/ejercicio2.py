################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedi
de una secuencia con números, retornando los valores como una tuple.
"""

def max_min_prom(secuencia):
    """Esta función recibe una secuencia de números y devuelve una tuple
    con los valores máximo, minimo y promedio"""
    maximo = secuencia[0]
    minimo = secuencia[0]
    suma = 0
    
    contador_max = len(secuencia) -1
    while contador_max >= 0:
        if secuencia[contador_max] > maximo:
            maximo = secuencia[contador_max]
        contador_max -= 1
    
    contador_min = len(secuencia) -1
    while contador_min >= 0:
        if secuencia[contador_min] < minimo:
            minimo = secuencia[contador_min]
        contador_min -= 1
    
    contador_prom = len(secuencia) -1
    while contador_prom >= 0:
        suma = suma + secuencia[contador_prom]
        contador_prom -= 1

    promedio = suma / len(secuencia)
    lista = (maximo, minimo, promedio)
    return tuple(lista)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = [int(x) for x in input("Ingrese multiples valores separados por ',': ").split(",")]
    resultado = max_min_prom(lista)
    print(f"De la lista {lista} el valor máximo es {resultado[0]}, el minimo es {resultado[1]} y el promedio es {resultado[2]}.")

if __name__ == "__main__":
    principal()
