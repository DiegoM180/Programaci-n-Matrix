# Tarea Semana 10 - Búsqueda y ordenación de elementos en arreglos multidimensionales
# Programa que ingresa 25 valores numéricos y los almacena en una matriz de 5x5

# 1. Crear una matriz de 5 filas por 5 columnas, inicializada en 0
matriz = [[0 for _ in range(5)] for _ in range(5)]

# 2. Solicitar al usuario los 25 valores y almacenarlos en la posición correspondiente
for i in range(5):
    for j in range(5):
        valor = int(
            input(f"Ingrese el valor para la posición [{i}][{j}]: ")
        )
        matriz[i][j] = valor

# 3. Mostrar todos los valores organizados en forma de matriz
print("\nMatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()
