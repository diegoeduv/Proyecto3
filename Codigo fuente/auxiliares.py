import hashlib
import getpass

def obtener_contraseña():
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    return hashlib.sha256(contraseña.encode()).hexdigest()

def escribir_fragmentos(archivo_salida, fragmentos):
    with open(archivo_salida, 'w') as f:
        for x, y in fragmentos:
            f.write(f"{x},{y}\n")

def leer_fragmentos(archivo_entrada):
    fragmentos = []
    with open(archivo_entrada, 'r') as f:
        for line in f:
            x, y = map(int, line.strip().split(','))
            fragmentos.append((x, y))
    return fragmentos

def validar_argumentos(n, t):
    if t > n or n <= 2:
        raise ValueError("Debe cumplir: 1 < t <= n y n > 2.")
