lista1 = [9, 8, 7]
lista2 = [5, 6, 7]

resultado = list(map(lambda lista1, lista2: lista1 + lista2, lista1, lista2))
print("O resultado será: ", resultado)