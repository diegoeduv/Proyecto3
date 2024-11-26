import pytest
import hashlib
from sympy import symbols
from shamir import generar_fragmentos, reconstruir_secreto

def test_generar_fragmentos():
    """
    Verifica que la función `generar_fragmentos` cree correctamente los fragmentos 
    y devuelva el secreto en su forma esperada.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        La función `generar_fragmentos` debe generar un secreto de 32 bytes y
        devolver exactamente `n` fragmentos, donde cada fragmento es una tupla
        con dos enteros.

    Precondiciones:
        La contraseña debe ser una cadena de texto válida, y los valores de `n` y `t`
        deben ser enteros positivos.

    Postcondiciones:
        Se aseguran las siguientes condiciones:
        1. El secreto generado tiene una longitud de 32 bytes.
        2. Se generan exactamente `n` fragmentos.
        3. Cada fragmento es una tupla con dos valores enteros.
    """
    contraseña = "mi_contraseña_segura"
    n = 5 
    t = 3 
    secreto, fragmentos = generar_fragmentos(contraseña, n, t)
    assert len(secreto) == 32, f"Secreto generado no tiene 32 bytes, tiene {len(secreto)}"
    assert len(fragmentos) == n, f"Se deben generar exactamente {n} fragmentos, pero se generaron {len(fragmentos)}"
    for fragmento in fragmentos:
        assert isinstance(fragmento, tuple) and len(fragmento) == 2, "Cada fragmento debe ser una tupla (x, y)"
        assert isinstance(fragmento[0], int) and isinstance(fragmento[1], int), "Los valores de cada fragmento deben ser enteros"

def test_reconstruir_secreto():
    """
    Prueba que la función `reconstruir_secreto` reconstruya correctamente el secreto
    con fragmentos suficientes.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        La función `reconstruir_secreto` debe devolver el mismo secreto original
        cuando se le pasan suficientes fragmentos.

    Precondiciones:
        Se deben generar al menos `t` fragmentos para poder reconstruir el secreto.

    Postcondiciones:
        El secreto reconstruido debe ser idéntico al secreto original generado con los fragmentos.
    """
    contraseña_prueba = "mi_contraseña_segura"
    n = 5  
    t = 3  
    secreto_original, fragmentos = generar_fragmentos(contraseña_prueba, n, t)
    fragmentos_a_utilizar = fragmentos[:t]
    secreto_reconstruido = reconstruir_secreto(fragmentos_a_utilizar)
    assert secreto_original == secreto_reconstruido, "El secreto reconstruido no coincide con el secreto original."


def test_reconstruir_secreto_con_pocos_fragmentos():
    """
    Verifica que se lance un error si se intenta reconstruir el secreto con menos de t fragmentos.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        La función `reconstruir_secreto` debe lanzar una excepción `ValueError` si se
        intenta reconstruir el secreto con menos de `t` fragmentos.

    Precondiciones:
        La cantidad de fragmentos disponibles debe ser inferior a `t`.

    Postcondiciones:
        Se lanza una excepción `ValueError` al intentar reconstruir el secreto con menos de `t` fragmentos.

    Excepciones:
        Lanza una excepción `ValueError` si se usan menos de `t` fragmentos.
    """
    contraseña = "mi_contraseña_segura"
    n = 5 
    t = 3 
    _, fragmentos = generar_fragmentos(contraseña, n, t)

    with pytest.raises(ValueError):
        reconstruir_secreto(fragmentos[:1])

def test_reconstruir_secreto_con_todos_los_fragmentos():
    """
    Verifica que se pueda reconstruir el secreto correctamente usando todos los fragmentos disponibles.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        La función `reconstruir_secreto` debe devolver el secreto original cuando se le
        pasan todos los fragmentos generados.

    Precondiciones:
        Se deben generar suficientes fragmentos para reconstruir el secreto.

    Postcondiciones:
        El secreto reconstruido debe ser idéntico al secreto original.
    """
    contraseña = "mi_contraseña_segura"
    n = 5  
    t = 3 
    secreto_original, fragmentos = generar_fragmentos(contraseña, n, t)
    secreto_reconstruido = reconstruir_secreto(fragmentos)
    assert secreto_original == secreto_reconstruido, "El secreto reconstruido no coincide con el original"

def test_hash_secreto():
    """
    Prueba que el hash del secreto generado a partir de la contraseña sea único.

    Parámetros:
        No recibe parámetros directamente.

    Resultados:
        La función `generar_fragmentos` debe generar secretos distintos para contraseñas diferentes.

    Precondiciones:
        Deben generarse fragmentos para dos contraseñas diferentes.

    Postcondiciones:
        El secreto generado a partir de la primera contraseña debe ser distinto del secreto generado
        con la segunda contraseña.
    """
    contraseña_prueba_1 = "contraseña1"
    contraseña_prueba_2 = "contraseña2"
    secreto_1, _ = generar_fragmentos(contraseña_prueba_1, 5, 3)
    secreto_2, _ = generar_fragmentos(contraseña_prueba_2, 5, 3)
    assert secreto_1 != secreto_2, "Los secretos generados para contraseñas diferentes deben ser distintos."
