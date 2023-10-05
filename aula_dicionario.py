#Pamela = {"nome" : "pamela",
#          "matricula":123,
#          "turma":"BHZM",
#          "notas": [10,8,10,9]}
#Carlos = {"nome" : "Carlos",
#         "matricula":124,
#         "turma":"BHZM",
#         "notas":[10,9,9,10]}

turma = []
turma.append({
          "nome" : "Pamela",
          "matricula":123,
          "turma":"BHZM",      
          "notas": [10,8,10,9]
})

turma.append({
          "nome" : "Carlos",
          "matricula":124,
          "turma":"BHZM",      
          "notas": []
})

for aluno in turma:
    print (aluno)

#--------------------
turma[1]["turma"] = "BHZT"
for aluno in turma:
    print (aluno)

for indice in range(0,5):
    turma[1]["notas"].append(float(input("Informe a nota:")))
print ( "Notas do:", turma[1]["nome"] , "-" , turma[1]["notas"])

#print(type(Pamela))
#print(type(Carlos))
#print(Pamela["nome"])
#print(Pamela["matricula"])

#for chave in Carlos:
 #   print(chave, Carlos[chave])
