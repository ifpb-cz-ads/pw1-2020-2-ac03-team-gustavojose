""" 5) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. """

print("A aritmética, como dizia, ou quase, o professor Girafales, é o ramo da matemática que estuda os números e as operações possíveis entre eles; forma a base da matemática mais complexa que utilizamos hoje em dia.")

numero1 = float(input("Informe um número: "))
numero2 = float(input("Informe outro valor: "))
operacao = str(input("Que operação desejas realizar? "))

if operacao == "+":
  resultado = numero1 + numero2
elif operacao == "-":
  resultado = numero1 - numero2
elif operacao == "*":
  resultado = numero1 * numero2
elif operacao == "/":
  resultado = numero1 / numero2

print(f"O resultado de {numero1:.3f} {operacao} {numero2:.3f} é igual a {resultado:.3f}.")
