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

print(collatz(1))
print(collatz(2))
print(collatz(3))

    

