import random

def crear_album(figus_total):
    album=[0 for i in range(figus_total)]
    return album

def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False
    
def comprar_figu(figus_total):
    return random.randint(0,figus_total-1)

def cuantas_figus(figus_total):
    count=0
    album=crear_album(figus_total)
    while album_incompleto(album):
        album[comprar_figu(figus_total)]+=1
        count+=1
    return count

def experimento_figus(n_repeticiones, figus_total):
    vector=[cuantas_figus(figus_total) for i in range(n_repeticiones)]
    promedio=sum(vector)/n_repeticiones
    return promedio

def comprar_paquete(figus_total, figus_paquete):
    paquete=[comprar_figu(figus_total) for i in range(figus_paquete)]
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    count=0
    album=crear_album(figus_total)
    while album_incompleto(album):
        paquete=comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu]+=1
        count+=1
    return count

def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    vector=[cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
    promedio=sum(vector)/n_repeticiones
    return promedio


