import hashlib
from Crypto.Cipher import AES
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
    cipher = AES.new(clave, AES.MODE_EAX)
    with open(archivo, "rb") as file:
        archivo_cifrado = cipher.encrypt(file.read())
    with open(archivo, "wb") as file:
        file.write(archivo_cifrado)

def cifrar(archivo_evaluaciones, evaluaciones, minimos, archivo, contraseña):
    # A partir de la contraseña, obtenemos su código hash con SHA-256
    hash = hashlib.sha256(contraseña.encode()).digest()
    hash_num = int.from_bytes(hash, byteorder='big')
    # Obtenemos n numeros aleatorios para evaluar el polinomio
    evaluaciones = []
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
    cifrar_AES(archivo, hash)
    

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

def descifrar_AES(archivoAES, clave):
    # Desciframos el archivo con AES
    cipher = AES.new(clave, AES.MODE_EAX)
    with open(archivoAES, "rb") as file:
        archivo_descifrado = cipher.decrypt(file.read())
    with open(archivoAES, "wb") as file:
        file.write(archivo_descifrado)
    

def descifrar(archivoAES, archivoEvaluaciones):
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
    clave = interpolacion_lagrange(valores_x, valores_y)
    # Desciframos el archivo con AES
    descifrar_AES(archivoAES, clave)
