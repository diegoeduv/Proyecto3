import random
from sympy import symbols, interpolate, Poly
import hashlib

def generar_fragmentos(contraseña: str, n: int, t: int):
    
    secreto = int.from_bytes(hashlib.sha256(contraseña.encode('utf-8')).digest(), 'big')

    
    secreto = secreto & ((1 << 256) - 1)
    
    coeficientes = [secreto] + [random.randint(0, (1 << 256) - 1) for _ in range(t - 1)]
    
    fragmentos = []
    for x in range(1, n + 1):
        y = sum(coef * (x ** i) for i, coef in enumerate(coeficientes)) % (1 << 256)
        fragmentos.append((x, y))

    
    return secreto.to_bytes(32, 'big'), fragmentos


