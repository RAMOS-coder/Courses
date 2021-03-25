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
    
P = float(input('Digite o seu peso em Kg: '))
Alt = float(input('Digite a sua altura(m): '))
print('')

IMC = P / (Alt * Alt)
pesoIdealH = (72.7 * Alt) - 58
pesoIdealW = (62.1 * Alt) - 44.7

if (IMC < 16):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Baixo peso muito grave')
    print('O seu peso ideal é entre ')
    print("")

    if (sexo == 1):
        print(f'O seu peso ideal é {pesoIdealH:.3}Kg')
    else:
        print(f'O seu peso ideal é {pesoIdealW:.3}Kg')
elif (IMC >= 16) and (IMC <= 16.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Baixo peso grave')
    print("")

    if (sexo == 1):
        print(f'O seu peso ideal é {pesoIdealH:.3}Kg')
    else:
        print(f'O seu peso ideal é {pesoIdealW:.3}Kg')
elif (IMC >= 17) and (IMC <= 18.49):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Baixo peso')
    print("")
    
    if (sexo == 1):
        print(f'O seu peso ideal é {pesoIdealH:.3}Kg')
    else:
        print(f'O seu peso ideal é {pesoIdealW:.3}Kg')
elif (IMC >= 18.5) and (IMC <= 24.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Peso ideal, parabéns!')
elif (IMC >= 25) and (IMC <= 29.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Sobrepeso')
    print("")

    if (sexo == 1):
        print(f'O seu peso ideal é {pesoIdealH:.3}Kg')
    else:
        print(f'O seu peso ideal é {pesoIdealW:.3}Kg')
elif (IMC >= 30) and (IMC <= 34.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Obesidade grau I')
    print("")

    if (sexo == 1):
        print(f'O seu peso ideal é {pesoIdealH:.3}Kg')
    else:
        print(f'O seu peso ideal é {pesoIdealW:.3}Kg')
elif (IMC >= 35) or (IMC <= 39.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Obesidade grau II')
    print("")

    if (sexo == 1):
        print(f'O seu peso ideal é {pesoIdealH:.3}Kg')
    else:
        print(f'O seu peso ideal é {pesoIdealW:.3}Kg')
elif (IMC > 40):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Obesidade grau III (Obesidade mórbida)')
    print("")

    if (sexo == 1):
        print(f'O seu peso ideal é {pesoIdealH:.3}Kg')
    else:
        print(f'O seu peso ideal é {pesoIdealW:.3}Kg')

