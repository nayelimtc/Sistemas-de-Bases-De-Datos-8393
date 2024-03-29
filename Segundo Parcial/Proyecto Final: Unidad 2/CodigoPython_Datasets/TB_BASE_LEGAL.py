# -*- coding: utf-8 -*-
"""Tb_Base_Legal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1juYv3bp7OfvwUztp0dUZrcD6xFC2J1kN

**Proyecto Final: Unidad 2**

****Entidad: Tb_Base_Legal****
"""

#Faker es un paquete de Python que genera datos falsos.
!pip install Faker

#Librerías necesarias para la generación de datos.
import pandas as pd
import uuid
import random
from faker import Faker
import datetime

#Librerías para generar cadena de numeros
import random as r
from random import seed
import string

#Librerías para generar fechas
from random import randint
from datetime import datetime

#Variable asignada para el tamaño del conjunto de datos. 
num_iess = 5000

#Lista de 7 características (Atributos)
features = [
    "VAR_ID_BASELEGAL",
    "VAR_DESCRIPCION_BASELEGAL",
    "VAR_DECRETO_BASELEGAL",
    "VAR_ESTADO_BASELEGAL",
    "VAR_ID_AFILIACION",
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**id_base_legal**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_base_legal.
df['VAR_ID_BASELEGAL'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada base_legal. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['VAR_ID_BASELEGAL'].nunique()==num_iess)

"""**descripcion_base_legal**"""

#Creamos la variale para la descripción de tipo string junto con su longitud de 
#cadena de caracteres
bio=[]
length_of_string = 20

for i in range(0, num_iess):#Creamos la descripcion de la universidad
  random.seed(datetime.now())
  #La descripcion contendra todo tipo de caracteres.
  bio=(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for i in range(length_of_string)))
  #Guardamos la descripcion en el atributo DescripcionUn
  df.VAR_DESCRIPCION_BASELEGAL[i] =bio

"""**decreto_base_legal**"""

#Los diferentes nombres de decretos.
VAR_DECRETO_BASELEGAL = ['Ley Orgánica del Sistema Nacional de Contratación Pública','Ley de Seguridad Social','Norma Creación','Normal de Regulación']
#Creacion de los permisos para cada una de las filas
df['VAR_DECRETO_BASELEGAL'] = random.choices(
  VAR_DECRETO_BASELEGAL, 
    weights=(30,40,20,5), 
    k=num_iess
)

"""**estado_base_legal**"""

#Los diferentes nombres de roles.
VAR_ESTADO_BASELEGAL = ['Activo','Inactivo']
#Creacion de los permisos para cada una de las filas
df['VAR_ESTADO_BASELEGAL'] = random.choices(
  VAR_ESTADO_BASELEGAL, 
    weights=(40,10), 
    k=num_iess
)

"""**id_afiliacion**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_perfil.
df['VAR_ID_AFILIACION'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['VAR_ID_AFILIACION'].nunique()==num_iess)

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('TB_BASELEGAL.csv')