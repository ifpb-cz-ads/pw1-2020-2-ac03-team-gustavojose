""" 7) Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir. """

print("A medida de kWh equivale à quantidade de kW consumidos a cada hora, e é igual também a 3600 quilojoules. Este utilitário vai calcular o preço a se pagar pelo consumo de energia elétrica de acordo com o tipo específico de residência na qual a corrente está sendo consumida.")

kWh = int(input("Informe a quantidade de quilowatt-hora consumido(s): "))
tipo = str(input("Informe agora o tipo de instalação (R para residências | I para indústrias | C para comércios): "))

if tipo == "R":
  if kWh <= 500:
    preco = 0.40 * kWh
  else:
    preco = 0.65 * kWh
elif tipo == "C":
  if kWh <= 1000:
    preco = 0.55 * kWh
  else:
    preco = 0.60 * kWh
elif tipo == "I":
  if kWh <= 5000:
    preco = 0.55 * kWh
  else:
    preco = 0.60 * kWh

print(f"O preço a se pagar será o equivalente ao valor de R$ {preco:.2f}.")
