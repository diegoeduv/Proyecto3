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
2.-Compila el programa principal con: javac Ejecutable.java
3.-Ejecuta el programa con: java Ejecutable
4. Al ejecutarse, el programa te pedirá que ingreses el nombre del archivo seguido de la bandera. Para la entrada se tiene que escribir: 11838.jpg s, con esto el programa calculará el índice de cobertura nubosa y además generará una imagen una imagen en blanco y negro llamada: imagen-seg.png y se guardara en la carpeta Imagenes. Si en la entrada únicamente se coloca: 11838.jpg, el programa solo calculará el índice de cobertura nubosa.


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
