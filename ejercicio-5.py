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

def sum_fil(matriz, fila):
    sumaF = 0
    for j in range(len(matriz[fila])):  # Itera sobre las columnas de la fila especificada
        sumaF += matriz[fila][j]  # Suma el elemento en la fila especificada
    return sumaF



if __name__ == "__main__":
    # Solicitar dimensiones de la matriz
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    matrizOg = matrix(filas, columnas)

    # Mostrar la matriz generada
    print("\nMatriz original:")
    matrix_to_screen(matrizOg)
    fila = int(input("\nIngrese el índice de la columna que desea sumar: "))
    fila = fila - 1 # se cambia a un numero que utilice el intervalo de las columnas 0 a 1

    # Validar que la fila exista en la matriz
    if fila < 0 or fila >= len(matrizOg[0]):
        print("Error: El índice de la fila está fuera de rango.")
    else:
        # Sumar los elementos de la fila
        sum_fila = sum_fil(matrizOg, fila)
        print("\nSuma columna ", fila+1 ,":", sum_fila)


   