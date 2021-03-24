P = float(input('Digite o seu peso em Kg: '))
Alt = float(input('Digite a sua altura(m): '))
print('')

IMC = P / (Alt * Alt)

if (IMC < 16):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Baixo peso muito grave')

    if (Alt >= 152) and (Alt < 154):
        print('Seu peso ideal é entre 45.5Kg à 56.8Kg')
elif (IMC >= 16) and (IMC <= 16.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Baixo peso grave')
elif (IMC >= 17) and (IMC <= 18.49):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Baixo peso')
elif (IMC >= 18.5) and (IMC <= 24.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Peso ideal, parabéns!')
elif (IMC >= 25) and (IMC <= 29.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Sobrepeso')
elif (IMC >= 30) and (IMC <= 34.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Obesidade grau I')
elif (IMC >= 35) or (IMC <= 39.99):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Obesidade grau II')
elif (IMC > 40):
    print(f'O seu IMC é: {IMC:.3}Kg/m²')
    print('Você está: Obesidade grau III (Obesidade mórbida)')

