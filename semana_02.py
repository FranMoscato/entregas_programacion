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

#ejercicio 4

def propagar(L):
    LQ=L.copy()
    quemados=[]
    fuegos=[]

    for ind,val in enumerate(L):
        if val==-1:
            quemados.append(ind)
        if val==1:
            fuegos.append(ind)

    if len(fuegos)>0:
        if len(quemados)==0:
            for p in range(len(LQ)):
                LQ[p]=1
        else:
            a_quemar=[]
            for i in range(len(quemados)):
                if i==0: #me fijo si hay fuegos entre inicio y primer quemado
                    for f in fuegos:
                        if f<quemados[i]:
                            a_quemar.append([-1,quemados[i]])#ponemos -1 porq despues vamos a hacer un +1 (queda 0)
                            break
                else:
                    for f in fuegos: #me fijo entre el ultimo quemado y el actual
                        if f<quemados[i] and f>quemados[i-1]:
                            a_quemar.append([quemados[i-1],quemados[i]])
                            break
                if i==len(quemados)-1: #me fijo entre ultimo quemado y el final
                    for f in fuegos: 
                        if f>quemados[i]:
                            a_quemar.append([quemados[i],len(LQ)])
                            break

            for par in a_quemar:
                for j in range(par[0]+1,par[1]):
                    LQ[j]=1
    
    return LQ

casos_prueba = [
    ([0, 1, 0], [1, 1, 1]),
    ([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0], [1, 1, -1, 0]),
    ([0, 1, -1, 0, 0, 1, 0], [1, 1, -1, 1, 1, 1, 1]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([-1, -1, -1], [-1, -1, -1]),
    ([1, 0, 0, 0, 1], [1, 1, 1, 1, 1]),
    ([1, -1, 0, 1, -1, 0, 1], [1, -1, 0, 1, -1, 1, 1]),
    ([-1, 0, 1, 0, -1], [-1, 1, 1, 1, -1]),
    ([], []),
]

for entrada, esperado in casos_prueba:
    resultado = propagar(entrada)
    print(f"Entrada: {entrada} -> Resultado: {resultado} -> {'✅ Correcto' if resultado == esperado else '❌ Incorrecto'}")