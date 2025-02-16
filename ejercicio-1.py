import random

def matrix(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.randint(1, 10)  # Genera un valor aleatorio dentro de uno y diez
            fila.append(valor)
        matriz.append(fila)
    return matriz

def matrix_to_screen(matriz):
    for i in range(len(matriz)): 
        print(matriz[i])

def sum_matrix(m1, m2):
    filas = len(m1)
    columnas = len(m1[0])
    matrizr = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matrizr[i][j] = m1[i][j] + m2[i][j]#se suman los elementos de misma posicion
    return matrizr

def sus_matrix(m1, m2):
    filas = len(m1)
    columnas = len(m1[0])
    matrizr = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matrizr[i][j] = m1[i][j] - m2[i][j]# se restan los elementos de misma
    return matrizr


if __name__ == "__main__":
    # Solicitar dimensiones de las matrices
    filasUno = int(input("Ingrese el número de filas de la primera matriz: "))
    columnasUno = int(input("Ingrese el número de columnas de la primera matriz: "))
    filasDos = int(input("Ingrese el número de filas de la segunda matriz: "))
    columnasDos = int(input("Ingrese el número de columnas de la segunda matriz: "))

    if filasUno != filasDos or columnasUno != columnasDos:
            print("Error: Las matrices no tienen el mismo tamaño. No se pueden operar.")
    else:
        matrizUno = matrix(filasUno, columnasDos)
        matrizDos = matrix(filasUno, columnasDos)

    # Mostrar las matrices generadas
    print("\nMatriz 1:")
    matrix_to_screen(matrizUno)
    print("\nMatriz 2:")
    matrix_to_screen(matrizDos)
    # Operar las matrices
    matrizsum = sum_matrix(matrizUno, matrizDos)
    print("\nResultado de la suma:")
    matrix_to_screen(matrizsum)
    matrizsus = sus_matrix(matrizUno, matrizDos)
    print("\nResultado de la resta:")
    matrix_to_screen(matrizsus)