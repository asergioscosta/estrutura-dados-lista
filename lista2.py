def listaxy(x, y):
    lista = []
    for i in range(x+1, y):
        lista.append(i)
    lista.insert(0, x)
    lista.append(y)
    return lista

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
lista = listaxy(x, y)
print(lista)