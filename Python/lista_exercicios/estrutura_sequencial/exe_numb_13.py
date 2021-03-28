print("======== Qual seu sexo? ========")

i = 0

while (i >= 1) or (i <= 2):
    sexo = int(input("1 - Masculino | 2 - Feminino: "))

    if (sexo != 1) and (sexo != 2):
        print("")
        print("Opção inválida! Por favor, escolha a opção 1 ou 2.")
        print("")
    else:
        print("")
        break

Alt = float(input('Digite a sua altura(m): '))
print('')

pesoIdealH = (72.7 * Alt) - 58
pesoIdealW = (62.1 * Alt) - 44.7

if (sexo == 1):
    print(f'O seu peso ideal é {pesoIdealH:.3}Kg')
else:
    print(f'O seu peso ideal é {pesoIdealW:.3}Kg')