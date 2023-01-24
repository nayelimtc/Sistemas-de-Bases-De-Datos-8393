# -*- coding: utf-8 -*-
"""Tb_Aportacion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eSHlif_IThV3nZymRNkBck1PjaEVWHO9

**Proyecto Final: Unidad 2**

**Entidad: Tb_Aportacion**
"""

#Faker es un paquete de Python que genera datos falsos.
!pip install Faker

"""DATOS SINTETICOS DE LA ENTIDAD PROVEE

Antes de iniciar cualquier codificacion se comenzara cargando las bibliiotecas con las cuales se crearan los datos
"""

#Librerías necesarias para lageneracion de datos
import pandas as pd
import uuid
import random
from faker import Faker
import datetime

#Librerías para generar cadena de números
import string
import random as r
from random import seed
from datetime import datetime

#Variable asignada para el tamaño del conjunto de datos
num_iess = 5000

"""     - Int_id_aportacion: una cadena única de caracteres para identificar la aportacion
     - Dt_fecha_aportacion: formato de cadena de año-mes-día
     - Int_no_aportacion: numero aleatorio de la cantidad de aportaciones realizadas por la persona
     - Var_detalle_aportacion: descripcion de el fin que tiene la aportacion
     - Var_monto_aportacion: cantidad de dinero aportado al IESS


"""

#Lista con los atributos
features = [
    "VAR_ID_APORTACION",
    "DT_FECHA_APORTACION",
    "INT_NO_APORTACION",
    "VAR_DETALLE_APORTACION",
    "VAR_MONTO_APORTACION",
    "ci_persona",
]#Creamos un dataframe para estos atributos
df = pd.DataFrame(columns=features)

"""**id_aportacion**"""

#Biblioteca uuid para generar cadena aleatoria de datos para id_afiliacion
df['VAR_ID_APORTACION'] = [uuid.uuid4().hex for i in range(num_iess)]

#Genera identificaciones únicas para cada usuario. Si todas las ID en el conjunto de datos son únicas, devuelve True.
print(df['VAR_ID_APORTACION'].nunique()==num_iess)

#Variable para los géneros para la creación de los nombres.
genero = ["female", "male"]

#Nombres.
df['genero']= random.choices(
    genero, 
    weights=(30,30), 
    k=num_iess)

"""**fecha_aportacion**"""

def DT_FECHA_APORTACION(start, end, n):
    #Formato de marca de tiempo (año, mes, dia)
    frmt = "%d-%m-%Y"
    #Formateo de los dos períodos de tiempo.
    stime = datetime.strptime(start, frmt)
    etime = datetime.strptime(end, frmt)
    
    #Se crea el grupo para tiempos aleatorios.
    td = etime - stime
    
    #Se genera una lista con los tiempos aleatorios.
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]
    return times
df['DT_FECHA_APORTACION'] = DT_FECHA_APORTACION("01-01-2020", "23-01-2023", num_iess)

"""**no_aportacion**"""

aportacion=[]
#Cantidad de números para la cadena..
size = 2
for i in range(0, num_iess):
  random.seed(datetime.now())
  #Números opcionales para formar la cadena.
  valores = [1,2,3,4,5,6,7,8,9,0]
  aportacion=(''.join([str(random.choice(valores)) for i in range(size)]))
  #Se guarda los números en telefonocallcenter.
  df.INT_NO_APORTACION[i]=aportacion

"""**monto_aportacion**"""

aportacion=[]
#Cantidad de números para la cadena..
size = 3
for i in range(0, num_iess):
  random.seed(datetime.now())
  #Números opcionales para formar la cadena.
  valores = [1,2,3,4,5,6,7,8,9,0]
  aportacion=(''.join([str(random.choice(valores)) for i in range(size)]))
  #Se guarda los números en telefonocallcenter.
  df.VAR_MONTO_APORTACION[i]=aportacion

"""**detalle_aportacion**"""

#Los diferentes nombres de estados.
VAR_DETALLE_APORTACION= ['Primera aportación puntual','Monto de aportes', 'Problema con tercera aportación','No realizo la décima aportación','Revisar mínimo de aportes']
#Creacion de los permisos para cada una de las filas
df['VAR_DETALLE_APORTACION'] = random.choices(
  VAR_DETALLE_APORTACION, 
    weights=(10,10,20,10,10), 
    k=num_iess
)

"""**ci_persona**"""

cedula=[]
#Cantidad de números para la cadena..
size = 10
for i in range(0, num_iess):
  random.seed(datetime.now())
  #Números opcionales para formar la cadena.
  valores = [0,1,2,3,4,5,6,7,8,9]
  cedula=(''.join([str(random.choice(valores)) for i in range(size)]))
  #Se guarda los números en telefonocallcenter.
  df.ci_persona[i]=cedula

#Eliminar genero, no es necesaerio para esta entidad.
del(df['genero'])

#Eliminar genero, no es necesaerio para esta entidad.
del(df['ci_persona'])

#Visualizar en la tabla los datos generados antes de descargar el excel.
df.head(5)

#Generar excel de los datos.
df.to_csv('TB_APORTACION.csv')