'''
6)	Faça um programa que receba dez números e armazene em uma lista. 
Em seguida solicite um outro número e armazene em uma variável chamada multiplicador. Percorra todo a lista e multiplique cada número pelo multiplicador e apresente em tela
'''

lista = [0]*10

for i in range(10):
    print('Digite um número: ')
    lista[i] = int(input())

multiplicador = int(input('Digite o número multiplicador: '))

for i in range(10):
    print (f'{lista[i]} x {multiplicador} = {lista[i]*multiplicador}')



print(f'Sua nova lista é: {lista}')
