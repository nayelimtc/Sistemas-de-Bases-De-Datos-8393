# -*- coding: utf-8 -*-
"""TB_PERFIL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nrrd3Ht7i2HzOxWT2VcylkyuULVGEAmS

**Proyecto Final: Unidad 1**

**Tb_Perfil**
"""

#Faker es un paquete de Python que genera datos falsos.
!pip install Faker

#Librerías necesarias para la generación de datos.
import pandas as pd
import uuid
import random
from faker import Faker
import datetime

#Librerías necesarias para el detalle o la descripción.
import string
import random
from random import seed
from datetime import datetime

#Variable asignada para el tamaño del conjunto de datos. 
num_iess = 5000

#Lista de 3 características (Atributos)
features = [
    "INT_ID_PERFIL",
    "VAR_DESCRIPCION_PERFIL",
    "VAR_NOMBRE_PERFIL",
    "INT_ID_USUARIO"
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**INT_ID_PERFIL**"""

#Biblioteca uuid para generar cadena aleatoria de datos.
df['INT_ID_PERFIL'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['INT_ID_PERFIL'].nunique()==num_iess)

"""**VAR_DESCRIPCION_PERFIL**"""

#Los diferentes nombres de roles.
VAR_DESCRIPCION_PERFIL = ['Creado hace 2 años','Creado hace 3 años','Creado hace 4 años','Creado hace 5 años','Creado hace 6 años','Creado hace 7 años','Creado hace 8 años','Creado hace 9 años','Creado hace 10 años','Creado hace 11 años']
#Creacion de los permisos para cada una de las filas.
df['VAR_DESCRIPCION_PERFIL'] = random.choices(
  VAR_DESCRIPCION_PERFIL, 
    weights=(50,50,50,50,50,50,50,50,50,50), 
    k=num_iess
)

"""**VAR_NOMBRE_PERFIL**"""

#Los diferentes nombres de roles.
VAR_NOMBRE_PERFIL = ['Usuario', 'Administrador']
#Creacion de los permisos para cada una de las filas
df['VAR_NOMBRE_PERFIL'] = random.choices(
  VAR_NOMBRE_PERFIL, 
    weights=(25,25), 
    k=num_iess
)

"""**INT_ID_USUARIO**"""

#Biblioteca uuid para generar cadena aleatoria de datos.
df['INT_ID_USUARIO'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['INT_ID_USUARIO'].nunique()==num_iess)

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('TB_PERFIL.csv')