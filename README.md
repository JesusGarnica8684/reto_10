# Reto 10

1. Desarrolle un programa que permita realizar la [suma/resta de matrices](https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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

```

2. Desarrolle un programa que permita realizar el [producto de matrices](https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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

```

3. Desarrolle un programa que permita obtener la  [matriz transpuesta](https://es.wikipedia.org/wiki/Matriz_transpuesta) de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
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

    # Mostrar la matriz generada
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


   
```

5. Desarrollar un programa que sume los elementos de una fila dada de
una matriz.

```python
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


   
```

