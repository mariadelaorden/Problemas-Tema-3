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
    if len(botellas) <= 1 :
        if botellas and corchos and tamano_correcto(botellas[0], corchos[0]):
            return [(botellas[0], corchos[0])]
        else :
            return []
        
    # Seleccionar una botella de inicio
    botella_inicial = botellas[0]

    # Dividir los corchos en dos grupos: corchos más grandes y corchos más pequeños
    corchos_adecuados = []
    corchos_grandes = []
    corchos_pequenos = []

    for corcho in corchos: 
        comparo = comparar(botella_inicial, corcho)
        if comparo == 0:
            corchos_adecuados.append(corcho)
        elif comparto < 0:
            corchos_pequenos.append(corcho)
        else:
            corchos_grandes.append(corcho)

    if not corchos_adecuados :
        return []
    
    corcho_adecuado = corchos_adecuados[0]
    corchos.remove(corcho_adecuado)