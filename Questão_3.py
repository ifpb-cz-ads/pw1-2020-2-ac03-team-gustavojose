salario = float(input('Informe o seu salario: '))
aumento = 0

if salario > 1250:
    aumento = salario*10/100
    print('O valor do aumento é de {}'.format(aumento))
else:
    aumento = salario*15/100
    print('O valor do aumento é de {}'.format(aumento))