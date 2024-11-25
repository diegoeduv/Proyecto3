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
