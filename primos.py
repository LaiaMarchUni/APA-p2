"""
Módulo de gestión de números primos.
Laia March Cervantes

Tests unitarios:
>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""


def esPrimo(numero):
    """
    Devuelve True si el argumento es primo, y False si no lo es.

    Argumentos:
        numero (int): Número natural mayor que uno.

    Retorna:
        bool: True si es primo, False en caso contrario.

    Excepciones:
        TypeError: Si el número no es un entero mayor que 1.
    """
    # Validación
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que uno.")

    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
            
    return True

    
def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.

    Argumentos:
        numero (int): Límite superior (no incluido).
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.

    Argumentos:
        numero (int): Número a descomponer.
    """
    factores = []
    d = 2
    temp = numero
    while temp > 1:
        while temp % d == 0:
            factores.append(d)
            temp //= d
        d += 1
        if d * d > temp and temp > 1:
            factores.append(temp)
            break
    return tuple(factores)

    
def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    f1 = descompon(numero1)
    f2 = descompon(numero2)
    
    # Conjunto de factores comunes 
    comunes = set(f1) & set(f2)
    
    resultado = 1
    for f in comunes:
        # Contamos cuántas veces aparece el factor en cada número
        # y nos quedamos con la menor cantidad (menor exponente)
        veces = min(f1.count(f), f2.count(f))
        resultado *= (f ** veces)
        
    return resultado

    
def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    f1 = descompon(numero1)
    f2 = descompon(numero2)
    
    todos = set(f1) | set(f2)
    
    resultado = 1
    for f in todos:
        veces = max(f1.count(f), f2.count(f))
        resultado *= (f ** veces)
        
    return resultado

    
def mcd(*numeros):
    """
    Devuelve el máximo común divisor de un número arbitrario de argumentos.
    """
    if not numeros: return 0
    
    # Obtenemos las descomposiciones de TODOS los números
    descomposiciones = [descompon(n) for n in numeros]
    
    # Los factores comunes deben estar en el primer número Y en todos los demás
    # Usamos set.intersection para encontrar los comunes a todos
    comunes = set(descomposiciones[0])
    for d in descomposiciones[1:]:
        comunes &= set(d)
        
    resultado = 1
    for f in comunes:
        # Para el MCD, buscamos el mínimo exponente entre todos los números
        veces = min(d.count(f) for d in descomposiciones)
        resultado *= (f ** veces)
        
    return resultado

    
def mcm(*numeros):
    """
    Devuelve el mínimo común múltiplo de un número arbitrario de argumentos.
    """
    if not numeros: return 0
    
    descomposiciones = [descompon(n) for n in numeros]
    
    # Para el MCM, necesitamos TODOS los factores que aparezcan al menos una vez
    todos_los_factores = set()
    for d in descomposiciones:
        todos_los_factores |= set(d)
        
    resultado = 1
    for f in todos_los_factores:
        # Buscamos el máximo exponente entre todos los números
        veces = max(d.count(f) for d in descomposiciones)
        resultado *= (f ** veces)
        
    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    