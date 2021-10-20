import numpy as np
import sympy as sym
from sympy import Matrix
import matplotlib.pyplot as plt
import math
import re
from colorama import Fore, Back, Style
import sys 
import os

from sympy.utilities.iterables import bracelets
#os.environ['PWD']

print("***** DISCLAIMER *****\n En caso de error al correr el programa, es porque la matriz aleatoria utilizada como llave de encriptación no cumple con las caracteristicas de una matriz reversible.\n Favor intentar nuevamente!")

def print_matrix_inFile():
    path = '$PWD'
    file0 = open('llave.txt','a')
    ma = clave.tolist()
    file0.write("\n"+''.join(map(str, ma)))
    file0.close()


# Matriz clave random para encriptar
import random

while True: 
    clave = np.array([[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)]])
    if  np.linalg.det(clave) != 0: break


# Introducir valores
try:
    s = input("Ingrese el mensaje a encriptar (solo se permiten letras y espacios): ")
    if not re.match("^[a-zA-Z\s]+$", s):
        print(Fore.RED + 'No se permiten caracteres especiales')
        # Error a proposito:
        sys.exit()
        
except:
    sys.exit()

s = s.lower()
list(s)
m=[]

print_matrix_inFile()

# Convertir cada letra del abecedario en un equivalente numerico; a=0,b=1,j=9, espacio=26...
for character in s:
    # Para el espacio
    if ord(character) == 32:
        number = ord(character) - 6
        m.append(number)
    else:
        number = ord(character) - 97
        m.append(number)


# Convertir matriz en mx3
columnas = len(m)
filas = columnas / 3
filas = math.ceil(filas)
matriz = np.array(m)
matriz = np.resize(matriz, (filas,3))


# Encriptar matriz
encriptar = matriz@clave
encriptar = np.remainder(encriptar, 27)
matriz_encriptada = encriptar


# Encriptar mensaje
en = []
encriptar = np.resize(encriptar, (1, columnas))
int_array = encriptar.tolist()

y = ''.join(map(str, int_array))
y = y.replace("[","")
y = y.replace("]","")
y = y.split(", ")
z = y

sclist = [int(j) for j in z]
for chara in sclist:
        letter = chara
        letter = chr(letter)
        en.append(letter)
    
str1=""
for ele in en: 
        str1 += ele
print("\nMensaje encriptado:\n", str1)


# Inversa de la matriz clave para desencriptar
inverse_clave = Matrix(clave).inv_mod(27)
inverse_clave = np.array(inverse_clave)
inverse_clave = inverse_clave.astype(float)

# Desencriptar mensaje
final = (matriz_encriptada@inverse_clave)%27
final = np.remainder(final, 27).flatten()
final = final[:columnas]

mensaje = []
for i in final.tolist():
    if i == 26:
        letter = i + 6
        letter = int(letter)
        letter = chr(letter)
        mensaje.append(letter)
    else:
        letter = i + 97
        letter = int(letter)
        letter = chr(letter)
        mensaje.append(letter)

str2=""
for ele in mensaje: 
        str2 += ele
print("\nMensaje desencriptado:\n", str2)

print("\nMatriz para encriptado:\n ", clave)

#b
plt.plot(clave)
plt.xlabel('X')
plt.ylabel('Y')

plt.plot(clave)
plt.plot(clave,'bo')
plt.legend(['Gráfica matriz llave'])
plt.show()