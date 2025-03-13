import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Actividad2:
    def __init__(self, data):
        datos = [(0,1),(0,2),(0,3),(0,4),(0,5)(0,6),(0,7),(0,8),(0,9),(0,10)]
        self.df = pd.DataFrame(data=datos, columns=["x", "y"])

# Introducción y cálculos con los arrays de NumPy
# 1. Genera un array con valores desde 10 hasta 29
array1 = np.arange(10, 30)
print("Array de 10 a 29:", array1)

# 2. Suma de todos los elementos en un array de 10x10 lleno de unos
array2 = np.ones((10, 10))
sum_array2 = np.sum(array2)
print("Suma de todos los elementos:", sum_array2)

# 3. Producto elemento a elemento entre dos arrays aleatorios de tamaño 5
array3 = np.random.randint(1, 11, 5)
array4 = np.random.randint(1, 11, 5)
product_array = array3 * array4
print("Producto elemento a elemento:", product_array)

# 4. Matriz de 4x4 con elementos i+j y su inversa
matrix = np.fromfunction(lambda i, j: i + j, (4, 4), dtype=int)
if np.linalg.det(matrix) != 0:
    inverse_matrix = np.linalg.inv(matrix)
    print("Matriz:", matrix)
    print("Inversa de la matriz:", inverse_matrix)
else:
    print("La matriz no tiene inversa.")

# 5. Valores máximo y mínimo en un array de 100 elementos aleatorios y sus índices
array5 = np.random.rand(100)
max_val = np.max(array5)
min_val = np.min(array5)
max_idx = np.argmax(array5)
min_idx = np.argmin(array5)
print("Máximo:", max_val, "en índice", max_idx)
print("Mínimo:", min_val, "en índice", min_idx)

# Broadcasting e indexado de Arrays
# 6. Suma de un array 3x1 y uno de 1x3 usando broadcasting
array6 = np.array([[1], [2], [3]])
array7 = np.array([[1, 2, 3]])
result = array6 + array7
print("Resultado del broadcasting:", result)

# 7. Extraer una submatriz 2x2 desde una matriz 5x5
matrix5x5 = np.random.randint(0, 10, (5, 5))
submatrix = matrix5x5[1:3, 1:3]
print("Matriz original:", matrix5x5)
print("Submatriz extraída:", submatrix)

# 8. Cambiar valores de índice 3 a 6 en un array de ceros a 5
array8 = np.zeros(10)
array8[3:7] = 5
print("Array modificado:", array8)

# 9. Invertir el orden de las filas de una matriz 3x3
matrix3x3 = np.random.randint(0, 10, (3, 3))
inverted_matrix = matrix3x3[::-1]
print("Matriz original:", matrix3x3)
print("Matriz con filas invertidas:", inverted_matrix)

# 10. Seleccionar elementos mayores a 0.5 en un array aleatorio de tamaño 10
array10 = np.random.rand(10)
selected_elements = array10[array10 > 0.5]
print("Elementos mayores a 0.5:", selected_elements) #hasta aqui bien

# Gráficos de dispersión, densidad y contorno
# 11. Gráfico de dispersión con dos arrays aleatorios de tamaño 100
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.title("Gráfico de dispersión")
plt.savefig("grafico.png")
plt.show()


# 12. Gráfico de dispersión con y = sin(x) + ruido gaussiano
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)
plt.scatter(x, y, label="Datos con ruido")
plt.plot(x, np.sin(x), color='r', label="y = sin(x)")
plt.legend()
plt.show()

# 13. Gráfico de contorno con np.meshgrid y función z = cos(x) + sin(y)
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.cos(X) + np.sin(Y)
plt.contour(X, Y, Z)
plt.title("Gráfico de contorno")
plt.show()

# 14. Gráfico de dispersión con 1000 puntos y color basado en densidad
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y, c=np.random.rand(1000), cmap='viridis')
plt.colorbar()
plt.show()

# 15. Gráfico de contorno lleno
plt.contourf(X, Y, Z, cmap='plasma')
plt.colorbar()
plt.show()

# 16. Añadir etiquetas y leyendas con código LaTex
plt.scatter(x, y, label=r'$Datos$')
plt.xlabel(r'$Eje\ X$')
plt.ylabel(r'$Eje\ Y$')
plt.title(r'$Gráfico\ de\ Dispersión$')
plt.legend()
plt.show()

# Histogramas
# 17. Histograma de 1000 números con distribución normal
hist_data = np.random.randn(1000)
plt.hist(hist_data, bins=30)
plt.show()

# 18. Histogramas de dos conjuntos de datos con distribuciones normales diferentes
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1.5, 1000)
plt.hist(data1, bins=30, alpha=0.5, label="Set 1")
plt.hist(data2, bins=30, alpha=0.5, label="Set 2")
plt.legend()
plt.show()

# 19. Experimentando con diferentes valores de bins
plt.hist(hist_data, bins=10, alpha=0.5, label="10 bins")
plt.hist(hist_data, bins=30, alpha=0.5, label="30 bins")
plt.hist(hist_data, bins=50, alpha=0.5, label="50 bins")
plt.legend()
plt.show()

# 20. Añadir línea vertical indicando la media
mean_value = np.mean(hist_data)
plt.hist(hist_data, bins=30)
plt.axvline(mean_value, color='r', linestyle='dashed', linewidth=2)
plt.show()

# 21. Histogramas superpuestos con transparencias
plt.hist(data1, bins=30, alpha=0.5, color='blue', label='Set 1')
plt.hist(data2, bins=30, alpha=0.5, color='red', label='Set 2')
plt.legend()
plt.show()



