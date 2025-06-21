def num_narcisista(numero):
    """Un numero narcisista es igual a la suma de sus digitos elevados
    a la potencia del numero de digitos.
    Ejemplo:
    153 es narcisista porque: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    Parametros:
    numero: int - El numero a evaluar
    Devuelve:
    bool - True si es narcisista, False si no lo es
    """
    
    # Se pasa el numero a string para trabajar con cada digito
    str_numero = str(numero)
    
    # S calcula el numero de digitos (n)
    n = len(str_numero)
    
    # Inicia la suma
    suma = 0
    
    # Por sobre cada digito del numero
    for digito in str_numero:
        # Se pasa el digito de vuelta a entero
        digito_int = int(digito)
        
        # Se suma el digito elevado a la potencia n
        suma += digito_int ** n
    
    # Comparamos la suma con el numero original
    return suma == numero

# Pruebas del algoritmo
print(num_narcisista(153))  # True (1^3 + 5^3 + 3^3 = 153)
print(num_narcisista(123))  # False (1^3 + 2^3 + 3^3 = 36 ≠ 123)