valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salario: '))
anos = int(input('Informe por quantos anos irá pagar: '))

valor_prestacao = valor_casa/(12*anos)
sobra_salario = salario*30/100

if valor_prestacao > sobra_salario:
    print('Empréstimo inviável')
else:
    print('Empréstimo disponivel')
