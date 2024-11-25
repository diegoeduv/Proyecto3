def interpolacion_lagrange(valores_x, valores_y):
    r = len(valores_x)
    clave = 0
    for i in range(r):
        polinomio_base = 1
        for j in range(r):
            if i != j:
                polinomio_base *= (-valores_x[j])/(valores_x[i]-valores_x[j])
        clave += polinomio_base * valores_y[i]
    return int(clave)       

def descifrar_AES(archivoAES, clave):
    # Desciframos el archivo con AES
    cipher = AES.new(clave, AES.MODE_EAX)
    with open(archivoAES, "rb") as file:
        archivo_descifrado = cipher.decrypt(file.read())
    with open(archivoAES, "wb") as file:
        file.write(archivo_descifrado)

def descifrar(archivoEvaluaciones, archivoAES):
    #Separamos las evaluaciones en 2 listas
    valores_x = []
    valores_y = []
    # Extraemos las evaluaciones del archivo
    with open(archivoEvaluaciones, "r") as file:
        for fila in file:
            x, y = map(int, fila.strip().split())
            valores_x.append(x)
            valores_y.append(y)
    # Generamos la clave a partir de las evaluaciones
    clave = interpolacion_lagrange(valores_x, valores_y)
    # Desciframos el archivo con AES
    descifrar_AES(archivoAES, clave)

    