"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
def min_max(numeros):
    numero_menor=numeros[0]
    numero_mayor=numeros[0]
    for numero in numeros:
        if numero<numero_menor:
            numero_menor=numero
        elif numero>numero_mayor:
            numero_mayor=numero
    resultado={
        "menor":numero_menor,
        "mayor":numero_mayor
    }
    return resultado

numeros=[5,7,9,2,1]
print(min_max(numeros))