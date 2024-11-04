# Función que recibe una lista de números y devuelve una lista con los mismos números pero ordenados de menor a mayor.
def ordenado_iterador(lista):
    if lista == []:
        return
    else:
        minimo = min(lista)
        lista.remove(minimo)
        yield minimo
        for elemento in ordenado_iterador(lista):
            yield elemento

lista = [1, 3, 3, 2, 1]

# Imprimir lista ordenada
for elemento in ordenado_iterador(lista):
    print(elemento)