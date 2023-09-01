'''
Faça um programa para corrigir provas de múltipla escolha com somatória. Cada prova tem dez questões e cada questão vale 1 ponto. 
O primeiro conjunto de dados a ser lido é o gabarito da prova. Os outros dados serão os números dos alunos e sua respectivas respostas.
Existem 15 alunos matriculados. Calcule e mostre:
- Para cada aluno seu número e sua nota;
- A percentagem de aprovação, sabendo-se que a nota mínima é 6,0

'''


gabarito = [0]*10

for i in range(10):
    print(f'digite o gabarito da questão {i+1}: ')
    gabarito[i] = int(input())

print(gabarito)
caprov = 0
for aluno in range (15):
    print('Aluno', aluno+1)
    mat = int(input('Digite a matrícula.'))
    nota = 0
    for j in range(10):
        print(f'Digite a resposta do aluno, {aluno+1}, para a questão {j+1}')
        resp = int(input())
        if resp == gabarito[j]:
            nota+=1
    print(f'Nota do aluno {aluno+1} = {nota}')    
    if nota>=6:
        caprov +=1

peraprov = (15*100)/caprov

print(f'O percentual de aprovados é de {peraprov}')
