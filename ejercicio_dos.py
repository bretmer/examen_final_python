"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def numero_primo(numero):
    if numero <2:
        return False
    for n in range(2,numero):
        if numero % 2==0:
            return False
    return True

lista_numeros=[2,5,7,9,5,8,11,3,7]
lista_filtrada=list(filter(numero_primo,lista_numeros))
print(lista_filtrada)
                    

