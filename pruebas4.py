def comparar (botella : int, corcho : int) -> int:
    """ Compara el tamaño de la botella y el corcho """
    if botella == corcho :
        return 0 # la botella es del tamaño del corcho
    elif botella < corcho :
        return -1 # la botella es más pequeña que el corcho
    else :
        return 1 # la botella es más grande que el corcho
    
def emparejar_corchos_botellas(botellas, corchos):
    if len(botellas) == 1:
        if comparar(botellas[0], corchos[0]):
            print(f"Tapar la botella {botellas[0]} con el corcho {corchos[0]}")
        else:
            print(f"El corcho {corchos[0]} no encaja en la botella {botellas[0]}")
    else:
        mitad = len(botellas) // 2
        botellas1, botellas2 = botellas[:mitad], botellas[mitad:]
        corchos1, corchos2 = corchos[:mitad], corchos[mitad:]

        emparejar_corchos_botellas(botellas1, corchos1)
        emparejar_corchos_botellas(botellas2, corchos2)

        combinar_resultados(botellas1, corchos1, botellas2, corchos2)

def combinar_resultados(botellas1, corchos1, botellas2, corchos2):
    for i in range(len(botellas1)):
        if comparar(botellas1[i], corchos1[i]):
            print(f"Tapar la botella {botellas1[i]} con el corcho {corchos1[i]}")
        else:
            print(f"El corcho {corchos1[i]} no encaja en la botella {botellas1[i]}")
    
    for i in range(len(botellas2)):
        if comparar(botellas2[i], corchos2[i]):
            print(f"Tapar la botella {botellas2[i]} con el corcho {corchos2[i]}")
        else:
            print(f"El corcho {corchos2[i]} no encaja en la botella {botellas2[i]}")

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

botellas4 = [5, 6, 7, 8]
corchos4 = [5, 6, 8]
emparejamiento4 = emparejar_corchos_botellas(botellas4, corchos4)
for botella4, corcho4 in emparejamiento4:
    print(f"Botella {botella4} emparejada con Corcho {corcho4}")



"""# Compara el elemento con el último de parte de la izquierda y el primero de la derecha 
    if derecha and elemento == derecha[0]:
        return [(elemento, derecha[0])] # si la lista derecha no está vacía compara el primer elemento de la lista de la derecha, si es igual, lo empareja
    elif izquierda and elemento == izquierda[-1]:
        return [(elemento, izquierda[-1])] # si la lista izquierda no está vacía compara el último elemento de la lista de la izquierda, si es igual, lo empareja
    elif izquierda and derecha and elemento < derecha[0]:
        return emparejar(elemento, izquierda) # si la lista izquierda y la derecha no están vacías compara el primer elemento de la lista de la derecha, si es menor es que se encuentra en la lista de la izquierda
    elif izquierda and derecha and elemento > izquierda[-1]:
        return emparejar(elemento, derecha) # si la lista izquierda y la derecha no están vacías compara el último elemento de la lista de la izquierda, si es mayor es que se encuentra en la lista de la derecha
    else:
        return []"""