################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de superposición entre dos
listas. Siendo 0 sin superposición y uno para cada elemento superpuesto.
"""

def grado_superposicion(lista, otra_lista):
    """Esta función recibe dos listas y retorna un número entero positivo que
    representa la cantidad de elementos presentes en ambas. """
    contador = len(lista)
    otro_contador = len(otra_lista)
    elem_lista = 0
    elem_lista_dos = 0
    superpuestos = 0
    if contador > otro_contador:
        while otro_contador > 0:
            if lista[elem_lista] == otra_lista[elem_lista_dos]:
                superpuestos += 1
            elem_lista += 1
            elem_lista_dos += 1
            otro_contador -= 1
    else:
        while contador > 0:
            if lista[elem_lista] == otra_lista[elem_lista_dos]:
                superpuestos += 1
            elem_lista += 1
            elem_lista_dos += 1
            contador -= 1
    return superpuestos
    
def principal():
    """
    Esta función pide por consola ingresar elementos separados por coma (", ") para confeccionar las
    dos listas que posteriormente compara y devuelve el grado de superposición entre las mismas.
    """
    lista_uno = input("Ingrese valores de la primera lista separados por ', ': ").split(", ")
    lista_dos = input("Ingrese valores de la segunda lista separados por ', ': ").split(", ")
    superpuestos = grado_superposicion(lista_uno, lista_dos)
    print(f"Hay {superpuestos} elementos superpuestos entre las listas {lista_uno} y {lista_dos}")

if __name__ == "__main__":
    principal()
