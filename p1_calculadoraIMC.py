
altura = float(input("Informe o valor da altura: "))
peso = float(input("Informe o peso: "))

imc = peso/(altura*altura)

print("IMC: " ,imc)
 
if imc < 18.5:
    print ("Abaixo do peso")
elif imc < 24.9:
    print("Peso Normal")
elif imc < 29.9:
    print("Sobrepeso")
else:
    print ("Obeso")

# if imc < 18.5 :
 #   print("Abaixo do Peso")

#else:
  #  if imc < 24.9 :
 #       print ("Peso Normal")
  #  else:
   #     if imc < 29.9:
    #        print ("Sobrepeso")
     #   else:
      #      print("Obeso")
print ("Fim")              