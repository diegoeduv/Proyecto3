import random
from sympy import symbols, interpolate, Poly
import hashlib

def generar_fragmentos(contraseña: str, n: int, t: int):
    """
    Genera fragmentos para el esquema de compartición de secretos usando una contraseña.

    Parámetros:
    - contraseña (str): La contraseña que se usará para generar el secreto.
    - n (int): Número total de fragmentos a generar.
    - t (int): Número mínimo de fragmentos requeridos para reconstruir el secreto.

    Retorno:
    - secreto (bytes): El secreto original, representado como 32 bytes.
    - fragmentos (list of tuples): Una lista de n fragmentos, donde cada fragmento representa un punto en el polinomio.
    """
    secreto = int.from_bytes(hashlib.sha256(contraseña.encode('utf-8')).digest(), 'big')

    
    secreto = secreto & ((1 << 256) - 1)
    
    coeficientes = [secreto] + [random.randint(0, (1 << 256) - 1) for _ in range(t - 1)]
    
    fragmentos = []
    for x in range(1, n + 1):
        y = sum(coef * (x ** i) for i, coef in enumerate(coeficientes)) % (1 << 256)
        fragmentos.append((x, y))

    
    return secreto.to_bytes(32, 'big'), fragmentos

def reconstruir_secreto(fragmentos):
    """
    Reconstruye el secreto original a partir de al menos t fragmentos.

    Parámetros:
    - fragmentos (list of tuples): Una lista de fragmentos, donde cada fragmento representa un punto en el polinomio. Se necesitan al menos t fragmentos para reconstruir.

    Retorno:
    - secreto (bytes): El secreto reconstruido, representado como 32 bytes.

    Excepciones:
    - ValueError: Si no se proporcionan suficientes fragmentos.
    """
    if len(fragmentos) < 2:
        raise ValueError("Se necesitan al menos 2 fragmentos para reconstruir el secreto.")

    valores_x, valores_y = zip(*fragmentos)
    
    x = symbols('x')

    polinomio_secreto = interpolate(list(zip(valores_x, valores_y)), x)
   
    secreto = Poly(polinomio_secreto).eval(0)

    secreto = secreto & ((1 << 256) - 1)

    secreto = int(secreto)  
    return secreto.to_bytes(32, 'big')
