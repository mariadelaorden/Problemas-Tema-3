"""

  q1  |  q2
  ---------
  q3  |  q4

"""

def divide(matriz):
    """ Divide una matriz cuadrada en 4 cuadrantes """
    def _divide(matriz, f_ini, f_fin, c_ini, c_fin):
        resultado = []
        cont_fila = 0
        for i in range(f_ini, f_fin):
            resultado += [[]]
            for j in range(c_ini, c_fin):
                resultado[cont_fila] += [matriz[i][j]]
            cont_fila += 1
        return resultado

    assert len(matriz) % 2 == 0 and len(matriz[0]) % 2 == 0, 'la matriz debe ser cuadrada'

    fin = len(matriz)
    medio = fin // 2
    
    q1 = _divide(matriz, 0, medio, 0, medio)
    q2 = _divide(matriz, 0, medio, medio, fin)

    q3 = _divide(matriz, medio, fin, 0, medio)
    q4 = _divide(matriz, medio, fin, medio, fin)

    return q1, q2, q3, q4

def combina(q1, q2, q3, q4):
    """ Combina los 4 cuadrantes """
    nueva_matriz = []
    for i in range(len(q2)):
        nueva_matriz.append(q1[i] + q2[i])
    for i in range(len(q4)):
        nueva_matriz.append(q3[i] + q4[i])
    return nueva_matriz

def transponer(matriz):
    "intercambia filas por columnas"
    if(len(matriz)==1):
        return matriz
    q1, q2, q3, q4 = divide(matriz)

    new_q1= transponer(q1)
    new_q2= transponer(q3)
    new_q3= transponer(q2)
    new_q4= transponer(q4)

    return combina(new_q1, new_q2, new_q3, new_q4)

def imprimir_matriz(matriz, nombres):
    "imprime la matriz con sus respectivos nombres"
    print("   " + " ".join(nombres))  
    print("  " + "-" * (4 * len(nombres)))  # Línea guiones

    # Imprimir filas con nombres
    for i, fila in enumerate(matriz):
        print(f"{nombres[i]:<3} | " + " ".join(map(str, fila))) #nombres con barra mas matriz

"Plzas: 1 si, 0 no "
"- ARO: puede ir a ruido, a sapo y a osa"
"- RUIDO: pude ir a osa "
"- OSA: puede ir a sapo"
"- SAPO: puede ir a aro y a osa"

print("P1: aro")
print("P2: ruido")
print("P3: osa")
print("P4: sapo")

plazas= ['P1', 'P2', 'P3', 'P4']
original = [[1, 1, 1, 1],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [1, 0, 1, 1]]

print("Callejero original:\n")
imprimir_matriz(original, plazas)
print("Nuevo callejero:\n")
nuevo = transponer(original)  #calcula el nuevo callejero
imprimir_matriz(nuevo, plazas)

