nota1 = float(input("Digite a 1 nota: "))
nota2 = float(input("Digite a 2 nota: "))
nota3 = float(input("Digite a 3 nota: "))
nota4 = float(input("Digite a 4 nota: "))
nota5 = float(input("Digite a 5 nota: "))

nota = (nota1, nota2, nota3, nota4, nota5)

soma = 0
for i in range(len(nota)):
    soma += nota[i]
media = soma / 5

print(" A média das notas é: ", media)