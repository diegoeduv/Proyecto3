import sys
import os
from cifrado_AES import encriptar_archivo
from shamir import generar_fragmentos
from auxiliares import escribir_fragmentos, obtener_contraseña, validar_argumentos

def main():
    if len(sys.argv) < 2:
        print("Uso: main.py [c|d] <otros argumentos>")
        sys.exit(1)

    modo = sys.argv[1]

    if modo == "c":  # Modo de cifrado
        if len(sys.argv) != 6:
            print("Uso: main.py c <documento.frg> <n> <t> <archivo_claro>")
            sys.exit(1)

        archivo_salida = sys.argv[2]
        n = int(sys.argv[3])
        t = int(sys.argv[4])
        archivo_entrada = sys.argv[5]

        validar_argumentos(n, t)

        contraseña = obtener_contraseña()
        clave, fragmentos = generar_fragmentos(contraseña, n, t)
        print(f"Clave generada: {clave.hex()}")  # Depuración clave generada
        for frag in fragmentos:
            print(f"Fragmento: {frag}")  # Depuración fragmentos

        archivo_encriptado = encriptar_archivo(archivo_entrada, clave)

        escribir_fragmentos(archivo_salida, fragmentos)
        print(f"Archivo cifrado generado: {archivo_encriptado}")
        print(f"Archivo de evaluaciones generado: {archivo_salida}")

        # Eliminar el archivo claro
        os.remove(archivo_entrada)
        print(f"Archivo original eliminado: {archivo_entrada}")
    
    elif modo == "d": 
        if len(sys.argv) != 4:
            print("Uso: main.py d <documento.frg> <archivo_cifrado>")
            sys.exit(1)
        
        input_shares = sys.argv[2]
        encrypted_file = sys.argv[3]

        shares = read_shares(input_shares)
        for share in shares:
            print("Fragmento leído: {share}")

        key = reconstruct_secret(share)
        print(f"Clave reconstruida: {key.hex()}")

        output_file = decrypt_file(encrypted_file, key)
        print (f"Archivo descifrado generado: {output_file}")

    else: 
        print("Modo desconocido. Use 'c' para cifrar o 'd' para descifrar.")
        sys.exit(1)

if __name__ == "__main__":
    main()
