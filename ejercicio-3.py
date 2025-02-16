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

def matriz_trans(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]  # Crea una matriz vacía con dimensiones invertidas
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]  # Intercambia filas por columnas
    return transpuesta


if __name__ == "__main__":
    # Solicitar dimensiones de las matrices
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matrizOg = matrix(filas, columnas)

    # Mostrar las matrices generadas
    print("\nMatriz original:")
    matrix_to_screen(matrizOg)

    # Operar las matrices
    matrizT = matriz_trans(matrizOg)
    print("\nMatriz transpuesta:")
    matrix_to_screen(matrizT)