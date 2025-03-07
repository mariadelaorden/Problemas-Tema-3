import io
import contextlib

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
    " Intercambia filas por columnas "
    if(len(matriz)==1):
        return matriz
    q1, q2, q3, q4 = divide(matriz)

    new_q1= transponer(q1)
    new_q2= transponer(q3)
    new_q3= transponer(q2)
    new_q4= transponer(q4)

    return combina(new_q1, new_q2, new_q3, new_q4)

def imprimir_matriz(matriz, nombres):
    " Imprime la matriz con sus respectivos nombres "
    print("    " + "  ".join(nombres))
    print("  " + "-" * (3 * len(nombres) + 1))  # Línea guiones

    # Imprimir filas con nombres
    for i, fila in enumerate(matriz):
        print(f"{nombres[i]:<3} | " + "  ".join(map(str, fila))) #nombres con barra mas matriz

"Plazas: 1 si, 0 no "
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
print("\nNuevo callejero:\n")
nuevo = transponer(original)  #calcula el nuevo callejero
imprimir_matriz(nuevo, plazas)

# Casos de prueba
matriz = [[1, 1, 1, 1],
          [0, 1, 1, 0],
          [0, 0, 1, 1],
          [1, 0, 1, 1]]
q1 = [1, 1, 1, 1]
q2 = [0, 1, 1, 0]
q3 = [0, 0, 1, 1]
q4 = [1, 0, 1, 1]
funcion_divide = divide(matriz)
funcion_combina = combina(q1, q2, q3, q4)
funcion_transponer = transponer(matriz)
funcion_imprimir = imprimir_matriz(matriz, plazas)
print(funcion_divide)
print(funcion_combina)
print(funcion_transponer)
print(funcion_imprimir)

def test_divide():
    matriz = [[1, 1, 1, 1],
              [0, 1, 1, 0],
              [0, 0, 1, 1],
              [1, 0, 1, 1]]
    q1 = [[1, 1], [0, 1]]
    q2 = [[1, 1], [1, 0]]
    q3 = [[0, 0], [1, 0]]
    q4 = [[1, 1], [1, 1]]
    res = (q1, q2, q3, q4)
    assert divide(matriz) == res

def test_combina():
    q1 = [[1, 1], [0, 1]]
    q2 = [[1, 1], [1, 0]]
    q3 = [[0, 0], [1, 0]]
    q4 = [[1, 1], [1, 1]]
    matriz = [[1, 1, 1, 1],
              [0, 1, 1, 0],
              [0, 0, 1, 1],
              [1, 0, 1, 1]]
    assert combina(q1, q2, q3, q4) == matriz

def test_transponer():
    matriz = [[1, 1, 1, 1],
              [0, 1, 1, 0],
              [0, 0, 1, 1],
              [1, 0, 1, 1]]
    matriz_transpuesta = [[1, 0, 0, 1],
                          [1, 1, 0, 0],
                          [1, 1, 1, 1],
                          [1, 0, 1, 1]]
    assert transponer(matriz) == matriz_transpuesta

def test_imprimir_matriz():
    matriz = [[1, 1, 1, 1],
              [0, 1, 1, 0],
              [0, 0, 1, 1],
              [1, 0, 1, 1]]
    nombres = ['P1', 'P2', 'P3', 'P4']
    salida_esperada = (
        "    P1  P2  P3  P4\n"
        "  -------------\n"
        "P1  | 1  1  1  1\n"
        "P2  | 0  1  1  0\n"
        "P3  | 0  0  1  1\n"
        "P4  | 1  0  1  1\n"
    )
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        imprimir_matriz(matriz, nombres)
    salida_obtenida = f.getvalue()
    assert salida_obtenida == salida_esperada, f"Error: esperado {salida_esperada}, pero se obtuvo {salida_obtenida}"