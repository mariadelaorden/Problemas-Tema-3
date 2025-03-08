def emparejar(elemento : int, lista : list[int]) -> list[tuple[int, int]]:
    """ Función que empareja un elemento con los elementos de una lista dividiéndola en dos partes """
    if not lista:
        return []
    
    # Divido la lista en dos partes
    medio = len(lista) // 2

    izquierda = lista[: medio]
    derecha = lista [medio : ]

    if derecha and elemento == derecha[0]:
        return [(elemento, derecha[0])] # si la lista derecha no está vacía compara el primer elemento de la lista de la derecha, si es igual, lo empareja
    elif izquierda and elemento == izquierda[-1]:
        return [(elemento, izquierda[-1])] # si la lista izquierda no está vacía compara el último elemento de la lista de la izquierda, si es igual, lo empareja
    elif izquierda and derecha : # si la lista izquierda y la derecha no están vacías
        if elemento < derecha[0]:
            return emparejar(elemento, izquierda) # compara el primer elemento de la lista de la derecha, si es menor es que se encuentra en la lista de la izquierda
        elif elemento > izquierda[-1]:
            return emparejar(elemento, derecha) # compara el último elemento de la lista de la izquierda, si es mayor es que se encuentra en la lista de la derecha
    
    return []
        
def emparejar_corchos_botellas(botellas : list[int], corchos : list[int]) -> list[tuple[int, int]]:
    """ Empareja corchos y botellas usando un algoritmo divide y vencerás """

    # Caso base: en caso de solo tener una botella y un corcho, verifica si son compatibles
    if not botellas or not corchos :
        return []
    elif len(botellas) == 1 and len(corchos) == 1:
        if botellas[0] == corchos[0]:
            return [(botellas[0], corchos[0])] # si el tamaño de la botella y el corcho coincice devuelve la botella con su corcho correspondiente
        else:
            return [] # si no son del mismo tamaño devuelve una lista vacía   

    medio_botellas = len(botellas) // 2
    medio_corchos = len(corchos) // 2

    botellas_izquierda = botellas[:medio_botellas]
    botellas_derecha = botellas[medio_botellas:]
    corchos_izquierda = corchos[:medio_corchos]
    corchos_derecha = corchos[medio_corchos:]

    # Aplico recursivamente el algoritmo de divide y vencerás
    emparejamientos_izquierda = emparejar_corchos_botellas(botellas_izquierda, corchos_izquierda)
    emparejamientos_derecha = emparejar_corchos_botellas(botellas_derecha, corchos_derecha)

    # Combino los resultados
    emparejamientos = emparejamientos_izquierda + emparejamientos_derecha

    # Emparejo los elementos restantes
    for botella in botellas_izquierda:
        emparejamientos.extend(emparejar(botella, corchos_derecha))
    for botella in botellas_derecha:
        emparejamientos.extend(emparejar(botella, corchos_izquierda))

    return emparejamientos        

# Casos de Prueba
botellas = [1, 3, 2, 4]
corchos = [1, 2, 4, 3]
emparejamiento = emparejar_corchos_botellas(botellas, corchos)
print(emparejamiento)

botellas1 = []
corchos1 = []
emparejamiento1 = emparejar_corchos_botellas(botellas1, corchos1)
print(emparejamiento1)

botellas2 = [1]
corchos2 = []
emparejamiento2 = emparejar_corchos_botellas(botellas2, corchos2)
print(emparejamiento2)

botellas3 = [1]
corchos3 = [3]
emparejamiento3 = emparejar_corchos_botellas(botellas3, corchos3)
print(emparejamiento3)

botellas4 = [5, 6, 7, 8]
corchos4 = [5, 6, 8]
emparejamiento4 = emparejar_corchos_botellas(botellas4, corchos4)
print(emparejamiento4)

# Test
def test_emparejar():
    # Prueba 1
    elem1 = 1
    lista1 = []
    res1 = []
    assert emparejar(elem1, lista1) == res1

    lista = [1, 2, 3, 4]

    # Prueba 2
    elem2 = 3
    res2 = [(3, 3)]
    assert emparejar(elem2, lista) == res2

    # Prueba 3
    elem3 = 2
    res3 = [(2, 2)]
    assert emparejar(elem3, lista) == res3

    # Prueba 4 
    elem4 = 1
    res4 = [(1, 1)]
    assert emparejar(elem4, lista) == res4

    # Prueba 5
    elem5 = 4
    res5 = [(4, 4,)]
    assert emparejar(elem5, lista) == res5

    # Prueba de que no haya o izquierda o derecha o ambas
    elem = 3
    list = [1, 2, 4]
    res = []
    assert emparejar(elem, list) == res

def test_emparejar_corchos_botellas():
    # Pruebo los casos base
    botellas1 = [2]
    corchos1 = [1]
    res1 = []
    assert emparejar_corchos_botellas(botellas1, corchos1) == res1

    botellas2 = []
    corchos2 = [1]
    res2 = []
    assert emparejar_corchos_botellas(botellas2, corchos2) == res2

    botellas3 = [1]
    corchos3 = [1]
    res3 = [(1, 1)]
    assert emparejar_corchos_botellas(botellas3, corchos3) == res3

    botellas4 = [1]
    corchos4 = [3]
    res4 = []
    assert emparejar_corchos_botellas(botellas4, corchos4) == res4

    # Pruebo la función
    botellas5 = [1, 4, 3, 2]
    corchos5 = [3, 2, 4, 1]
    res5 = [(1, 1), (4, 4), (3, 3), (2, 2)]
    assert emparejar_corchos_botellas(botellas5, corchos5) == res5

    botellas6 = [5, 6, 7, 8]
    corchos6 = [5, 6, 8]
    res6 = [(5, 5), (8, 8), (6, 6)]
    assert emparejar_corchos_botellas(botellas6, corchos6) == res6