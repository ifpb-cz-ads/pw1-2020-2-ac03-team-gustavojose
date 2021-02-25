numero1=float(input('Informe o primeiro numero: '))
numero2=float(input('Informe o segundo numero: '))
numero3=float(input('Informe o terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print('O maior numero é {}'.format(numero1))
elif numero2 > numero3:
    print('O maior numero é {}'.format(numero2))
else:
    print('O maior numero é {}'.format(numero3))

if numero1 < numero2 and numero1 < numero3:
    print('O menor numero é {}'.format(numero1))
elif numero2 < numero3:
    print('O menor numero é {}'.format(numero2))
else:
    print('O menor numero é {}'.format(numero3))
