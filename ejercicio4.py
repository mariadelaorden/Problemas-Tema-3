def comparar (botella : int, corcho : int) -> int:
    """ Compara el tamaño de la botella y el corcho """
    if botella == corcho :
        return 0 # la botella es del tamaño del corcho
    elif botella < corcho :
        return -1 # la botella es más pequeña que el corcho
    else :
        return 1 # la botella es más grande que el corcho

def emparejar_corchos_botellas(botellas : list[int], corchos : list[int]) -> list[tuple[int, int]]:
    """ Empareja corchos y botellas usando un algoritmo divide y vencerás """

    # Caso base: en caso de solo tener una botella y un corcho, verifica si son compatibles
    if len(botellas) == 1 and len(corchos) == 1 :
        if comparar(botellas[0], corchos[0]) == 0:
            return [(botellas[0], corchos[0])] # si el tamaño de la botella y el corcho coincice devuelve la botella con su corcho correspondiente
        else:
            return [] # si no son del mismo tamaño devuelve una lista vacía
    elif not botellas or not corchos :
        return []    

    # Divido en dos mitades los corchos y las botellas
    medio = len(botellas) // 2
    corchos_izq = botellas[:medio]
    corchos_dch = botellas[medio:]
    botellas_izq = botellas[:medio]
    botellas_dch = botellas[medio:]

    # Emparejar cada mitad de manera recursiva
    emparejamiento_izq = emparejar_corchos_botellas(botellas_izq, corchos_izq)
    emparejamiento_dch = emparejar_corchos_botellas(botellas_dch, corchos_dch)

    # Combinar los emparejamientos
    emparejamiento_total = emparejamiento_izq + emparejamiento_dch

    return emparejamiento_total

# Casos de Prueba
botellas = [1, 3, 2, 4]
corchos = [1, 2, 4, 3]
emparejamiento = emparejar_corchos_botellas(botellas, corchos)
for botella, corcho in emparejamiento:
    print(f"Botella {botella} emparejada con Corcho {corcho}")

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

# Test
def test_comparar():
    botella1 = 1
    corcho1 = 3
    botella2 = 1
    corcho2 = 1
    botella3 = 3
    corcho3 = 1
    assert comparar(botella1, corcho1) == -1
    assert comparar(botella2, corcho2) == 0
    assert comparar(botella3, corcho3) == 1

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
    res = [(1, 1), (4, 4), (3, 3), (2, 2) ]
    assert emparejar_corchos_botellas(botellas, corchos) == res