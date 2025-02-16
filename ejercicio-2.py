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

def mult_matrix(m1, m2):
    filas_m1 = len(m1)
    columnas_m1 = len(m1[0])
    columnas_m2 = len(m2[0])
    matrizr = [[0 for _ in range(columnas_m2)] for _ in range(filas_m1)]
    for i in range(filas_m1): # Itera sobre las filas de la primera matriz
        for j in range(columnas_m2): #Itera sobre las columnas de la segunda matriz
            for k in range(columnas_m1): # Itera para realizar la multiplicación y suma
                matrizr[i][j] += m1[i][k] * m2[k][j]
    return matrizr


if __name__ == "__main__":
    # Solicitar dimensiones de las matrices
    filasUno = int(input("Ingrese el número de filas de la primera matriz: "))
    columnasUno = int(input("Ingrese el número de columnas de la primera matriz: "))
    filasDos = int(input("Ingrese el número de filas de la segunda matriz: "))
    columnasDos = int(input("Ingrese el número de columnas de la segunda matriz: "))

    if filasDos != columnasUno:
            print("Error: La segunda matriz no tiene el mismo numero de elementos que columnas de la segunda matriz. No se pueden multiplicar.")
    else:
        matrizUno = matrix(filasUno, columnasDos)
        matrizDos = matrix(filasUno, columnasDos)

    # Mostrar las matrices generadas
    print("\nMatriz 1:")
    matrix_to_screen(matrizUno)
    print("\nMatriz 2:")
    matrix_to_screen(matrizDos)
    # Operar las matrices
    matrizmult = mult_matrix(matrizUno, matrizDos)
    print("\nResultado del producto de las matrices:")
    matrix_to_screen(matrizmult)