import hashlib
from random import randint

def generar_polinomio(minimos):
    # Generamos un polinomio de grado 'minimos - 1' con coeficientes aleatorios
    coeficientes = [randint(1, 100) for i in range(minimos - 1)]
    return coeficientes

def evaluacion_polinomio(polinomio, clave, x):
    resultado = polinomio[0]
    for i in range (1, len(polinomio)):
        resultado = resultado * (x + polinomio[i])
    resultado = resultado * (x + clave)
    return resultado

def cifrar_AES(archivo, clave):
    # Ciframos el archivo con AES
    pass

def cifrar(archivo_evaluaciones, evaluaciones, minimos, archivo, contraseña):
    # A partir de la contraseña, obtenemos su código hash con SHA-256
    hash = hashlib.sha256(contraseña.encode()).digest()
    # Obtenemos n numeros aleatorios para evaluar el polinomio
    numeros = [randint(1, 100) for j in range(evaluaciones)]
    polinomio = generar_polinomio(minimos)
    # Obtenemos las n evaluaciones del polinomio
    for i in range(evaluaciones):
        evaluaciones.append(evaluacion_polinomio(polinomio, hash, numeros[i]))
    # generamos el archivo con las evaluaciones separado por renglones
    with open(archivo_evaluaciones, "w") as file:
        for evaluacion in evaluaciones:
            file.write(str(evaluacion) + "\n")
    # ciframos el archivo con AES
    archivo_cifrado = cifrar_AES(archivo, hash)
    #generamos el archivo cirado con AES
    with open(archivo_cifrado, "wb") as file:
        file.write(archivo_cifrado)

def interpolacion_lagrange(valores_x, valores_y):
    # Obtenemos el polinomio de Lagrange
    n = len(valores_x)
    clave = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L = L * (valores_x[j]) / (valores_x[i] - valores_x[j])
        clave = clave + L * valores_y[i]
    return clave

def descifrar_AES(archivoEvaluaciones, archivoAES):
    # Extraemos las evaluaciones del archivo
    with open(archivoEvaluaciones, "r") as file:
        evaluaciones = file.readlines()
    #Separamos las evaluaciones en 2 listas
    valores_x = []
    valores_y = []
    for evaluacion in evaluaciones:
        valores_x.append(evaluacion[0])
        valores_y.append(evaluacion[1])
    # Generamos la clave a partir de las evaluaciones
    interpolacion_lagrange(valores_x, valores_y)
    # Desciframos el archivo con AES
    pass
