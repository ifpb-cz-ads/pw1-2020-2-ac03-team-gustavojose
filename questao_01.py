""" /* 1) Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h. */ """

print("No intuito de dirijir, o cidadão aceita andar conforme a legislação de trânsito do seu país. Isso significa que além de possuir o direito de ir e vir, há penalização caso alguma lei seja infligida. E uma delas é a de limite de velocidade.")

velocidade = float(input("Informe a velocidade do carro em km/h: "))

if velocidade > 80:
  multa = (velocidade - 80) * 5.00

  print("Você foi multado ;).")
  print(f"Estás devendo uma multa de R$ {multa:.2f}.")
else:
  print("Motorista prudente detectado.")
