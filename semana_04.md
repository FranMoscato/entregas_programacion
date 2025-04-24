# Análisis del Arbolado en Espacios Verdes – Semana 04

Para esta actividad, se utilizó el archivo 'arbolado-en-espacios-verdes.csv' proporcionado por el gobierno de CABA que contiene información sobre, como indica su nombre, el arbolado urbano en espacios verdes.

Utilizando Python, debimos realizar un análisis sobre el dataset y responder algunas preguntas:

---

## Preguntas y Resultados

A continuación, se presentan las preguntas planteadas junto con las respuestas obtenidas mediante el análisis del dataset:

### 1. ¿Cuál o cuáles son los parques con más cantidad de árboles?

**Respuesta:**  
El parque con más árboles es: **INDOAMERICANO**

### 2. ¿Cuál o cuáles son los parques con los árboles más altos en promedio?

**Respuesta:**  
El parque con los árboles más altos en promedio es: **INFANTE DON ENRIQUE EL NAVEGANTE**

### 3. ¿Cuál o cuáles son los parques con más variedad de especies?

**Respuesta:**  
El parque con mayor cantidad de especies distintas es: **EL ROSEDAL (Sector dentro de Plaza HOLANDA)**

### 4. ¿Cuál es la especie de árbol que tiene más ejemplares en toda la ciudad?

**Respuesta:**  
La especie con más ejemplares en los espacios verdes analizados es: **Eucalipto**

### 5. ¿Cuál es la razón entre árboles exóticos y árboles nativos?

**Respuesta:**  
La razón entre árboles exóticos y árboles nativos en los espacios verdes de Buenos Aires es de: **2.01287**

---

## Algunas consideraciones:

- En las preguntas **1**, **2** y **3** se descartaron los registros cuyo nombre figuraba como **"S/D"** (sin determinar).
- Para el cálculo de la razón entre árboles exóticos y nativos:
    - Se consideran nativas aquellas especies que en algún registro fueron clasificadas como nativas.
    - El resto de las especies son consideradas como exóticas.


---

## Código utilizado para esta sección:

```python
def _dicc_parques(nombre_archivo):
    """
    Crea un diccionario donde las Keys son los parques y como definicion tiene una lista compuesta como:[suma de alturas,lista de contadores por especie,lista de especies] 
    """
    dicc_parques={}
    with open(nombre_archivo, newline='',encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['espacio_ve'] not in dicc_parques.keys():
                dicc_parques[row['espacio_ve']]=[float(row['altura_tot']),[1],[row['nombre_com']]]
            else:
                if row['nombre_com'] in dicc_parques[row['espacio_ve']][2]:
                    dicc_parques[row['espacio_ve']][0]+=float(row['altura_tot'])
                    ind=dicc_parques[row['espacio_ve']][2].index(row['nombre_com'])
                    dicc_parques[row['espacio_ve']][1][ind]+=1
                else:
                    dicc_parques[row['espacio_ve']][0]+=float(row['altura_tot'])
                    ind=dicc_parques[row['espacio_ve']][2].append(row['nombre_com'])
                    dicc_parques[row['espacio_ve']][1].append(1)
    return dicc_parques

def buscar_maxi(diccionario):
    """"
    Dado un diccionario donde las definiciones son un valor numerico, devolvera la/las keys cuya definicion sean el maximo
    """
    top=[]
    maxi=max(diccionario.values())
    for key in diccionario.keys():
        if diccionario[key]==maxi:
            top.append(key)
    if len(top)>1:
        return top
    else:
        return top[0]

def parque_mas_arbolado(parques):
    """
    Devuelve el/los parque/s con mas arboles
    """
    count_tree={}
    for parque in parques.keys():
        if parque != 'S/D': #Entendemos que "sin determinar" no puede ser el parque con mas arboles
            count_tree[parque]=sum(parques[parque][1])

    return buscar_maxi(count_tree)
    
def parque_mas_alto(parques):
    """
    Devuelve el/los parque/s cuya altura promedio de arbol sea la mayor
    """
    count_tree={}
    for parque in parques.keys():
        if parque != 'S/D': #Entendemos que "sin determinar" no puede ser el parque con mas arboles
            count_tree[parque]=parques[parque][0]/sum(parques[parque][1])
        
    return buscar_maxi(count_tree)

def parque_mas_variado(parques):
    """
    Devuelve el/los parque/s con mayor cantidad de especies
    """
    count_tree={}
    for parque in parques.keys():
        if parque != 'S/D': #Entendemos que "sin determinar" no puede ser el parque con mas arboles
            count_tree[parque]=len(parques[parque][2]) 
    
    return buscar_maxi(count_tree)

def _contador_especies(parques):
    """
    Devuelve un diccionario donde las keys son cada especie de arbol y su definicion la cantidad de ejemplares en la ciudad
    """
    espe_dicc={}
    for parque in parques.keys():
        for ii in range(len(parques[parque][2])):
            if parques[parque][2][ii] in espe_dicc.keys():
                espe_dicc[parques[parque][2][ii]]+=parques[parque][1][ii]
            else:
                espe_dicc[parques[parque][2][ii]]=parques[parque][1][ii]
    return espe_dicc

def lista_nativo(nombre_archivo):
    """
    Devuelve una lista con las especies autoctonas
    """
    arboles_nativos=[]
    with open(nombre_archivo, newline='',encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['origen']=='Nativo/Autóctono' and row['nombre_com'] not in arboles_nativos:
                arboles_nativos.append(row['nombre_com'])
    return arboles_nativos

def ratio_nativos(nombre_archivo,espe_dicc):
    """
    Calcula el ratio entre arboles exoticos y nativos.
    """
    arboles_nativos=lista_nativo(nombre_archivo)
    cont_nativos=0
    cont_exo=0
    for especie in espe_dicc.keys():
        if especie in arboles_nativos:
            cont_nativos+=espe_dicc[especie]
        else:
            cont_exo+=espe_dicc[especie]
    
    return cont_exo/cont_nativos

def analisis_parques(nombre_archivo):

    """
    Funcion creada para correr e imprimir los analisis del ejercicio 5.
    """
    parques=_dicc_parques(nombre_archivo)
    print(f"El/Los parques con mas arboles son: {parque_mas_arbolado(parques)}")
    print(f"El/Los parques con arboles mas altos en promedio son: {parque_mas_alto(parques)}")
    print(f"El/Los parques con mayor cantidad de especies son: {parque_mas_variado(parques)}")
    espe_dicc=_contador_especies(parques)
    print(f"La/las especies con mas ejemplares son: {buscar_maxi(espe_dicc)}")
    print(f"La razon arboles exoticos sobre arboles nativos es: {ratio_nativos(nombre_archivo,espe_dicc)} ")
    
    return "Fin de analisis"
    
```