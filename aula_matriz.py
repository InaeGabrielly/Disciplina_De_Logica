lista_frutas = ['uva','maca','melancia']

exp_matriz = [[1],[6,9],[7,10,5]]
exp_matriz[0].append(5)   #add na ultima posicao
exp_matriz[1].insert(0,4) #insere em uma posiçao dada
exp_matriz[1][2] = 7      #altera um elemento
#exp_matriz.append([7,8,9])
#print (exp_matriz[-1][0])

#for linha in exp_matriz:
   # for elem in linha:
   #     print (elem)


for cont_linha in range(0,len(exp_matriz)):
    for cont_elem in range(0,len(exp_matriz[cont_linha])):
       exp_matriz [cont_linha][cont_elem] = 0
print (exp_matriz)

exp_matriz[1][0] = int(input("Informe um valor: "))
exp_matriz[1].append(int(input("Informe um valor: ")))
print (exp_matriz)