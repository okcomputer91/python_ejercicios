def separar_ordenar_pares_impares(lista):
    # Ordenar la lista en orden ascendente
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)

    # Separar en numers pares e impares 
    """(CORRECCIÓN 1: Operador módulo % en lugar de división /)"""
    pares = [num for num in lista_ordenada if num % 2 == 0]
    impares = [num for num in lista_ordenada if num % 2 != 0]  # antes era num/2 != 0 (incorrecto)

    # Ordena ambas listas en orden descendente 
    """
    (CORRECCIÓN 2: Typo en variable 'impares')"""
    pares_desc = sorted(pares, reverse=True)
    impares_desc = sorted(impares, reverse=True)  # antes decia 'inpares' (era un typo, tenia una n)

    print("Números pares en orden descendente:", pares_desc)
    print("Numeros impares en orden descendente:", impares_desc)
# Prueba 
"""(CORRECCIÓN 3: Usar lista [] y no lista()"""
lista = [5, 3, 8, 6, 7, 2]  # asi es como debe ser
separar_ordenar_pares_impares(lista)

    
