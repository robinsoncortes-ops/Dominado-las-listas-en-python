# funcion

def numeros_positivos(lista):
    contador = 0

    for numero in lista:
        if numero > 0:
            contador +=1

    return contador

numeros = [1,3,4,45]
resultado = numeros_positivos(numeros)
print("cantidad de numeros positivos:", resultado)
