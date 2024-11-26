Proyecto3-MYP Esquema de Secreto Compartido de Shamir
Este proyecto realiza el cifrado y descifrado de documentos con información confidencial con ayuda de una clave mediante el esquema de secreto compartido de Shamir.
#Requisitos:
Tener instalado:
1 Sympy
2 Pycryptodomex
3 Python
4 Pytest
5 Pip

#Instalación:
1. Instalación de Python:
Ubuntu:
sudo apt update
sudo apt install python3
Fedora:
sudo dnf install python3
2. Instalación de pip:
Ubuntu:
sudo apt install python3-pip
Fedora:
sudo dnf install python3-pip
3. Instalación de Sympy:
pip install sympy
4. Instalación de Pycryptodomex:
pip install pycryptodomex
5. Instalación de Pytest:
pip install pytest

#Uso: Para ejecutar el código sigue los siguientes pasos:
1.- Dirígete a la carpeta Codigo fuente con cd Codigo\ fuente/
2.-Se tiene un archivo de texto por defecto en la carpeta Archivos. Debes mover a esa carpeta todos los archivos que desees manejar. Si se quiere cifrar el archivo, ejecuta el programa de la siguiente manera: Python3 main.py c <nombreDelArchivoDeEvaluaciones.frg> <numeroDeClavesAGenerar> <numeroDeClavesMinimasParaDescifrar> <nombreDelArchivoACifrar.txt>
Ejemplo: python3 main.py c evaluaciones.frg 5 3 documento_claro.txt
Esto eliminará el archivo documento_claro.txt en la carpeta Archivos, y creará dentro de la misma el archivo ya cifrado, documento_claro.aes; así como el archivo que contiene las evaluaciones, evaluaciones.frg.
3.Si se quiere descifrar el archivoejecuta el programa de la siguientemanera: Python3 main.py d <nombreDelArchivoDeEvaluaciones.frg> <nombreDelArchivoCifrado.aes>
Ejemplo:python3 main.py d evaluaciones.frg documento_claro.aes
Esto recuperará el contenido original del archivo documento_claro.txt dentro de la carpeta Archivos.

#Tests: Para ejecutar las pruebas sigue los siguientes pasos:
1.- Dirígete a la carpeta Codigo fuente con cd Codigo\ fuente/
2.-Compilar y ejecutar las pruebas con los siguientes comandos, dependiendo que prueba se quiera ejecutar:
2.1 pytest test_auxiliares.py
2.2 pytest test_cifrado.py
2.3 pytest test_shamir.py
2.4 python -m unittest test_mainDePrueba.py

#Integrantes del equipo y sus roles:
Líder del equipo: diegoeduv
Backend:  brenda96011, diegoeduv, IvanGonzalezzz, tomasbh7
