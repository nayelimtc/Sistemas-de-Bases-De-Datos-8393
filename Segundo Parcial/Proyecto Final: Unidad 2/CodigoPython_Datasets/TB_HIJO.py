# -*- coding: utf-8 -*-
"""TB_HIJO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vjcaD6ZctvEuBwe47gmqgflPmPL45uek

**Proyecto Final: Unidad 1**

**Tb_hijo**
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
from datetime import datetime

#Variable asignada para el tamaño del conjunto de datos. 
num_iess = 5000

#Lista de 4 características (Atributos)
features = [
    "INT_ID_HIJO",
    "VAR_NOMBRE_HIJO",
    "VAR_EDAD_HIJO",
    "INT_ID_PERSONA",
]# Creando un DF para estas características
df = pd.DataFrame(columns=features)

"""**INT_ID_HIJO**"""

#Biblioteca uuid para generar cadena aleatoria de datos.
df['INT_ID_HIJO'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['INT_ID_HIJO'].nunique()==num_iess)

"""**VAR_NOMBRE_HIJO**"""

#Variable para los géneros para la creación de los nombres.
genero = ["female", "male"]

#Nombres.
df['genero']= random.choices(
    genero, 
    weights=(30,30), 
    k=num_iess)

#Instancia Faker
faker = Faker()
#Función.
def name_gen(genero):
    #Para masculino
    if genero=='male':
        return faker.name_male()
    #Para femenino
    elif genero=='female':
        return faker.name_female()
    #Genera los nombres
    return faker.name()
df['VAR_NOMBRE_HIJO'] = [name_gen(i) for i in df['genero']]

"""**VAR_EDAD_HIJO**"""

edad=[]
#Cantidad de números para la cadena..
size = 1 or 2
for i in range(0, num_iess):
  random.seed(datetime.now())
  #Números opcionales para formar la cadena.
  valores = [0,1,2,3,4,5,6,7,8,9]
  edad=(''.join([str(random.choice(valores)) for i in range(size)]))
  #Se guarda los números.
  df.VAR_EDAD_HIJO[i]=edad

"""**INT_ID_PERSONA**"""

#Biblioteca uuid para generar cadena aleatoria de datos.
df['INT_ID_PERSONA'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['INT_ID_PERSONA'].nunique()==num_iess)

#Eliminar genero, no es necesario para esta entidad.
del(df['genero'])

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('TB_HIJO.csv')