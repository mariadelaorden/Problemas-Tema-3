def comparar (botella : int, corcho : int) -> int:
    """ Compara el tamaño de la botella y el corcho """
    if botella == corcho :
        return 0 # la botella es del tamaño del corcho
    elif botella < corcho :
        return -1 # la botella es más pequeña que el corcho
    else :
        return 1 # la botella es más grande que el corcho
    
def emparejar_corchos_botellas(botellas: list[int], corchos: list[int]) -> list[tuple[int, int]]:
    """Empareja corchos y botellas usando un algoritmo divide y vencerás"""

    def dividir_y_vencer(botellas: list[int], corchos: list[int], resultado: list[tuple[int, int]]):
        # Caso base: si alguna lista está vacía, no se puede emparejar
        if not botellas or not corchos:
            return

        # Caso base: en caso de tener una sola botella y un solo corcho, verifica si son compatibles
        if len(botellas) == 1 and len(corchos) == 1:
            if comparar(botellas[0], corchos[0]) == 0:
                resultado.append((botellas[0], corchos[0]))
            return

        # Divide las listas en dos mitades
        medio_botellas = len(botellas) // 2
        medio_corchos = len(corchos) // 2

        # Divide y vencer: empareja las mitades
        dividir_y_vencer(botellas[:medio_botellas], corchos[:medio_corchos], resultado)
        dividir_y_vencer(botellas[medio_botellas:], corchos[medio_corchos:], resultado)

        # Combina los emparejamientos adicionales para asegurarse de no perder pares válidos
        i, j = 0, 0
        while i < len(botellas) and j < len(corchos):
            if comparar(botellas[i], corchos[j]) == 0:
                if (botellas[i], corchos[j]) not in resultado:
                    resultado.append((botellas[i], corchos[j]))
                i += 1
                j += 1
            elif comparar(botellas[i], corchos[j]) == -1:
                i += 1
            else:
                j += 1

    resultado = []
    dividir_y_vencer(botellas, corchos, resultado)
    return resultado

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