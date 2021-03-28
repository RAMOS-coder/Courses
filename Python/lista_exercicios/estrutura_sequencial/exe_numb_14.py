pesoPeixe = float(input('Quantos Kg de peixe: '))
print('')

if (pesoPeixe > 50):
    excesso = pesoPeixe - 50
    multa = excesso * 4

    print('O limite máximo de Kg de peixe permitido é de 50Kg')
    print(f'O excesso de Kg de peixe foi: {excesso:.1f}Kg')
    print('')
    print(f'A multa para essa penalidade é de R${multa:.2f}')
else:
    print('O limite máximo de Kg de peixe permitido é de 50Kg')
    print('Limite de Kg de peixe não excedido.')
