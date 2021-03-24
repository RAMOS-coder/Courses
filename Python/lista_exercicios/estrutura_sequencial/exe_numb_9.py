def main():

    print('Converter Fahrenheit para Celsius')
    print('')

    F = float(input('Digite a temperatura em Fahrenheit: '))

    C = 5 *((F - 32) /9)

    print(f'A temperatura {F}ºF é igual a {C:.1f}ºC')

main()