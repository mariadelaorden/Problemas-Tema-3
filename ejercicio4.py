def tamano_correcto (botella : int, corcho : int) -> int:
    """ Verificar si el tamaño de la botella y el corcho son iguales """
    return botella == corcho

def comparar (botella : int, corcho : int) -> int: 
    """ Compara el tamaño de la botella y el corcho """
    if botella == corcho:
        return 0 # el corcho es adecuado
    elif botella < corcho:
        return -1 # la botella es más pequeño que el corcho
    else :
        return 1 # la botella es más grande que el corcho

def taponar_botellas(botellas : list[int], corchos : list[int]) -> bool :
    """ Algoritmo principal para taponar las botellas """
    # Caso base: si solo hay una botella y un corchos, verifico si el corcho es adecuado para la botella
    if len(botellas) <= 1 :
        if botellas and corchos and tamano_correcto(botellas[0], corchos[0]):
            return [(botellas[0], corchos[0])]
        else :
            return []
        
    # Seleccionar una botella de inicio
    botella_inicial = botellas[0]

    # Dividir los corchos en dos grupos: corchos grandes, adecuados y pequeños
    corchos_adecuados = []
    corchos_grandes = []
    corchos_pequenos = []

    # Comparo los corchos con las botellas y los asigno a cada lista según corresponda
    for corcho in corchos: 
        comparo = comparar(botella_inicial, corcho)
        if comparo == 0:
            corchos_adecuados.append(corcho)
        elif comparo < 0:
            corchos_pequenos.append(corcho)
        else:
            corchos_grandes.append(corcho)

    # Si ningún corcho es adecuado, devolverá una lista vacía
    if not corchos_adecuados :
        return []
    
    # Encuentro el corcho adecuado y lo quito de la lista
    corcho_adecuado = corchos_adecuados[0]
    corchos.remove(corcho_adecuado)

    # Divido la lista a la mitad y recursivamente voy comprobando los corchos
    mitad_izquierda = taponar_botellas(botellas[1:], corchos_pequenos)
    mitad_derecha = taponar_botellas(botellas[1:], corchos_grandes)

    # Combino las soluciones
    mitades = [(botella_inicial, corcho_adecuado)] + mitad_izquierda + mitad_derecha

    return mitades


botellas = [1, 2, 3, 4]
corchos = [2, 4, 1, 3]
resultado = taponar_botellas(botellas, corchos)
print (resultado)