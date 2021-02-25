""" 4) Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas. """

print("Este programa vai calcular o preço da passagem de uma viagem de carro, custando cinquenta centavos para viagens de até duzentos quilômetros, e quarenta e cinco centavos para viagens mais longas, por quilômetro.")

distancia = float(input("Qual a distância do trajeto em quilômetros? "))

if distancia <= 200:
  custoDoKm = 0.50
else:
  custoDoKm = 0.45

preco = custoDoKm * distancia

print(f"O preço da passagem é de R$ {preco:.2f}.")
