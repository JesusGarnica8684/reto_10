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

def sum_column(matriz, columna):
    sumC = 0
    for fila in matriz:
        sumC += fila[columna]  # Suma el elemento en la columna especificada
    return sumC



if __name__ == "__main__":
    # Solicitar dimensiones de las matrices
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matrizOg = matrix(filas, columnas)

    # Mostrar las matrices generadas
    print("\nMatriz original:")
    matrix_to_screen(matrizOg)
    colum = int(input("\nIngrese el índice de la columna que desea sumar: "))
    colum = colum - 1 # se cambia a un numero que utilice el intervalo de las columnas 0 a 1

    # Validar que la columna exista en la matriz
    if colum < 0 or colum >= len(matrizOg[0]):
        print("Error: El índice de la columna está fuera de rango.")
    else:
        # Sumar los elementos de la columna
        sum_columna = sum_column(matrizOg, colum)
        print("\nSuma columna ", colum+1 ,":", sum_columna)


   