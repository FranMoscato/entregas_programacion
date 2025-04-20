import csv


def arboles_parque(nombre_archivo, nombre_parque):
    """
    Dado el nombre de un parque, esta funcion creara un diccionario donde las keys son los id de los arboles en el y sus definiciones los datos de ellos
    """
    dicc_tree={}
    with open(nombre_archivo, newline='',encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['espacio_ve']==nombre_parque:
                dicc_tree[row['id_arbol']]=row
    return dicc_tree

def arbol_mas_popular(nombre_parque):
    """
    Dado el nombre de un parque, devolvera el arbol mas popular del mismo (string). En caso de que haya mas de uno con la misma cantidad, devolvera una lista
    """
    dicc_tree=arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    count_tree={}
    for key in dicc_tree.keys():
        if dicc_tree[key]['nombre_com'] not in count_tree.keys():
            count_tree[dicc_tree[key]['nombre_com']]=1
        else:
            count_tree[dicc_tree[key]['nombre_com']]+=1
    
    popular=[]
    maxi=max(count_tree.values())
    for key in count_tree.keys():
        if count_tree[key]==maxi:
           popular.append(key)
    
    if len(popular)>1:
        return popular
    else:
        return popular[0]
    
def n_mas_altos2(nombre_parque, n):
    
    dicc_tree=arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)

    first=True
    ordenados=[]
    for key in dicc_tree.keys():
        if first:
            ordenados.append(key)
            first=False
        else:
            agg_qc=False
            for pos in range(len(ordenados)):
                if dicc_tree[key]['altura_tot'] >= dicc_tree[ordenados[pos]]['altura_tot'] and not agg_qc:
                    ordenados.insert(pos, key)
                    agg_qc=True
            if not agg_qc:
                ordenados.append(key)
    return (ordenados[:n])

def n_mas_altos(nombre_parque, n):
    """
    Devuelve los N arboles mas altos de un parque. No considera cuando hay mas de uno con la misma altura y hay que cortar
    """
    dicc_tree=arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    lista_alturas=[]
    for key in dicc_tree.keys():
        lista_alturas.append([float(dicc_tree[key]['altura_tot']),key])
    ordenada=sorted(lista_alturas, key=lambda tree: tree[0],reverse=True)
    if len(ordenada)>=n:
        return [item[1] for item in ordenada[:n]]
    else:
        return [item[1] for item in ordenada] #si no tiene N arbole, devuelve todos

def altura_promedio(nombre_parque, especie):
    """
    Dado el nombre de un parque y una especie, la funcion calculara la altura promedio de este tipo de arbol en el espacio verde indicado
    """
    dicc_tree=arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    lista_alturas=[]
    for key in dicc_tree.keys():
        if dicc_tree[key]['nombre_com']==especie:
            lista_alturas.append(float(dicc_tree[key]['altura_tot']))
    if len(lista_alturas)>0:
        return sum(lista_alturas)/len(lista_alturas)
    else:
        return 0
    
def lista_parques(nombre_archivo):
    """
    Esta funcion devolvera la lista de parques del archivo CSV
    """
    lista_parques=[]
    with open(nombre_archivo, newline='',encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['espacio_ve'] not in lista_parques:
                lista_parques.append(row['espacio_ve'])
    return lista_parques

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
    Calcula el ratio entre arboles exoticos y nativos
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
    parques=_dicc_parques(nombre_archivo)
    print(f"El/Los parques con mas arboles son: {parque_mas_arbolado(parques)}")
    print(f"El/Los parques con arboles mas altos en promedio son: {parque_mas_alto(parques)}")
    print(f"El/Los parques con mayor cantidad de especies son: {parque_mas_variado(parques)}")
    espe_dicc=_contador_especies(parques)
    print(f"La/las especies con mas ejemplares son: {buscar_maxi(espe_dicc)}")
    print(f"La razon arboles exoticos sobre arboles nativos es: {ratio_nativos(nombre_archivo,espe_dicc)} ")
    
    return "Fin de analisis"
        
if __name__=="__main__":
    #Este espacio es para pruebas
    #print(arboles_parque('arbolado-en-espacios-verdes.csv','AVELLANEDA, NICOLÁS, Pres.'))
    print(arbol_mas_popular('AVELLANEDA, NICOLÁS, Pres.'))
    print(n_mas_altos('AVELLANEDA, NICOLÁS, Pres.', 10))
    #print(n_mas_altos2('AVELLANEDA, NICOLÁS, Pres.', 10))
    print(altura_promedio('AVELLANEDA, NICOLÁS, Pres.','Jacarandá'))
    #print(lista_parques('arbolado-en-espacios-verdes.csv'))
    print(analisis_parques('arbolado-en-espacios-verdes.csv'))