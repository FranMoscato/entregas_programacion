#ejercicio 1

def invertir_lista(lista):
    lista_r=lista.copy()[::-1]
    return lista_r

#ejercicio 2
def collatz(nro):
        var=nro
        count=0
        while var!=1:
            if var%2==0:
                var=var/2
            else:
                var=var*3+1
            count+=1
        return count

#ejercicio 3
def contar_definiciones(d):
    claves=d.keys()
    new_dicc={}
    for clave in claves:
        new_dicc[f'{clave}']=len(d[f'{clave}'])
    return new_dicc

def cantidad_de_claves_letra(d, l):
    claves=d.keys()
    count=0
    for clave in claves:
        if clave[0]==l:
            count+=1
    return count

d={'hola':['javier','susana'],'mama':['sofia'],'hapa':[]}
print(d)
print(contar_definiciones(d))
print(cantidad_de_claves_letra(d,'l'))