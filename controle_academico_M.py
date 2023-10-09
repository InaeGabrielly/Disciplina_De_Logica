displinas=["Algoritmos","Segurança", "Desenv. Web"]
turma = []
def cadastro_aluno (nome ,matricula, idade):
    aluno = {
    
    "matricula": matricula,
    "idade": idade,
    "nome": nome,
    "notas" :  [[],[],[]]
    }
    
    turma.append(aluno)

def encontra_aluno(matricula):
    for aluno in turma:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def inicializa_notas(matricula):
    aluno = encontra_aluno(matricula)
    for notas in aluno["notas"]:
        for item_nota in range (0,5):
            notas.append(0)

def valida_nota(nota):   
    if nota < 0 or nota > 10:
        return False
    return True

def insere_notas(matricula, cod_disc):
    aluno = encontra_aluno(matricula)
    for nota in range (0,5):
        mensagem = "Informe a nota" + str(nota + 1)+ ":"
        nota_temporaria = float(input(mensagem))
        while not valida_nota(nota_temporaria):
            nota_temporaria = float(input(mensagem))
        aluno["notas"][cod_disc][nota] = nota_temporaria

cadastro_aluno("Carlos",123,19)
inicializa_notas(123)

cadastro_aluno("Guilherme",124,25)
inicializa_notas(124)
insere_notas(124, 0)
#print(encontra_aluno(124))

for aluno in turma:
 print (aluno)

