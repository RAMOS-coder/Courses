def main():
    
    print('Cálculo de Horas Trabalhadas')
    print('')

    hGan = float(input('Quanto você ganha por hora? '))
    hTrab = float(input('Quantas horas trabalhadas por mês? '))

    salTot = hGan * hTrab

    print(f'Seu salário referido a este mês é: R$ {salTot:.2f}')

main()