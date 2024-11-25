import pytest
import hashlib
from sympy import symbols
from shamir import generar_fragmentos, reconstruir_secreto

def test_generar_fragmentos():
    """
    Verifica que la función `generar_fragmentos` cree correctamente los fragmentos 
    y devuelva el secreto en su forma esperada.
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
    """
    contraseña_prueba_1 = "contraseña1"
    contraseña_prueba_2 = "contraseña2"
    secreto_1, _ = generar_fragmentos(contraseña_prueba_1, 5, 3)
    secreto_2, _ = generar_fragmentos(contraseña_prueba_2, 5, 3)
    assert secreto_1 != secreto_2, "Los secretos generados para contraseñas diferentes deben ser distintos."
