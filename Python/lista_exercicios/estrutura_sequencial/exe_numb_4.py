def main():

    print("Média de 4 notas bimestrais")

    nota1 = input("Digite a sua primeiro nota:")
    nota2 = input("Digite a sua segunda nota: ")
    nota3 = input("Digite a sua terceira nota: ")
    nota4 = input("Digite a sua quarta nota: ")

    soma = float(nota1) + float(nota2) + float(nota3) + float(nota4)
    media = soma / 4

    print("A média das suas notas é {: .1f}".format(media))

main()