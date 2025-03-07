def emparejar(elemento : int, lista : list[int]) -> list[tuple[int, int]]:
    """ Función que empareja un elemento con los elementos de una lista dividiéndola en dos partes """
    if not lista:
        return []
    
    # Divido la lista en dos partes
    medio = len(lista) // 2

    izquierda = lista[: medio]
    derecha = lista [medio : ]

    for elem in izquierda + derecha:
        if elemento == elem:
            return [(elemento, elem)]
    return []
        
def emparejar_corchos_botellas(botellas : list[int], corchos : list[int]) -> list[tuple[int, int]]:
    """ Empareja corchos y botellas usando un algoritmo divide y vencerás """

    # Caso base: en caso de solo tener una botella y un corcho, verifica si son compatibles
    if not botellas or not corchos :
        return []
    elif len(botellas) == 1 and len(corchos) == 1 :
        if botellas[0] == corchos[0]:
            return [(botellas[0], corchos[0])] # si el tamaño de la botella y el corcho coincice devuelve la botella con su corcho correspondiente
        else:
            return [] # si no son del mismo tamaño devuelve una lista vacía   

    emparejamientos = []

    if len(corchos) >= len(botellas):
        for botella in botellas:
            emparejamientos.extend(emparejar(botella, corchos))
    else :
        for corcho in corchos:
            emparejamientos.extend(emparejar(corcho, botellas))

    return emparejamientos        

# Casos de Prueba
botellas = [1, 3, 2, 4]
corchos = [1, 2, 4, 3]
emparejamiento = emparejar_corchos_botellas(botellas, corchos)
print(emparejamiento)

botellas1 = []
corchos1 = []
emparejamiento1 = emparejar_corchos_botellas(botellas1, corchos1)
for botella1, corcho1 in emparejamiento1:
    print(f"Botella {botella1} emparejada con Corcho {corcho1}")

botellas2 = [1]
corchos2 = []
emparejamiento2 = emparejar_corchos_botellas(botellas2, corchos2)
for botella2, corcho2 in emparejamiento2:
    print(f"Botella {botella2} emparejada con Corcho {corcho2}")

botellas3 = [1]
corchos3 = [3]
emparejamiento3 = emparejar_corchos_botellas(botellas3, corchos3)
for botella3, corcho3 in emparejamiento3:
    print(f"Botella {botella3} emparejada con Corcho {corcho3}")

botellas4 = [5, 6, 7, 8]
corchos4 = [5, 6, 8]
emparejamiento4 = emparejar_corchos_botellas(botellas4, corchos4)
for botella4, corcho4 in emparejamiento4:
    print(f"Botella {botella4} emparejada con Corcho {corcho4}")

# Test

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

    # Pruebo la función
    botellas = [1, 4, 3, 2]
    corchos = [3, 2, 4, 1]
    res = [(1, 1), (4, 4), (3, 3), (2, 2)]
    assert emparejar_corchos_botellas(botellas, corchos) == res