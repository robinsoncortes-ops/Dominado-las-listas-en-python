# funcion

def obtene_primero_ultimo(lista):
    if lista:
        if(len(lista)>=2):
            return(lista[0], lista[-1])
        else:
            return "litas no tiene elementos suficientes"
    else:
        return "datos no validos. lista vacia"

# invocar funcion
lista_1 = [1,2,3,4]
resultado = obtene_primero_ultimo(lista_1)
print(resultado)