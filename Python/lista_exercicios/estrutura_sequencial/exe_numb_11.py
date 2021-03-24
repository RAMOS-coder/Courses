N1 = int(input('Digite um número inteiro: '))
N2 = int(input('Digite outro número inteiro: '))
N3 = float(input('Agora digite um número real (Ex: 15.5): '))
print('')

Result1 = (N1 * 2) / N2
Result2 = (N1 * 3) + N3
Result3 =  N3 ** 3

print(f'O dobro do {N1} com metade do {N2} é: {Result1:.0f}')
print('')
print(f'A soma do triplo do {N1} com o {N3} é: {Result2:.1f}')
print('')
print(f'O {N3} elevado ao cubo é: {Result3:.2f}')