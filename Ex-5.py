'''
5)	Faça um programa que receba dez números e armazene em uma lista. 
Em seguida percorra toda a lista e procure qual o MAIOR valor dentro da lista e qual o MENOR valor dentro da lista. No final apresente o MAIOR e o MENOR valor.
'''

lista = [0]*10
omaior = 0
c = 0


for i in range(10):
    print('Digite um número')
    lista[i] = int(input())
    if omaior < lista[i]:
        omaior = lista[i]
    if c == 0:
        omenor = lista[i]
    elif lista[i] < omenor: 
        omenor = lista[i]
    c += 1

print(f'O menor número digitado foi: {omenor}')
print(f'O maior número digitado foi: {omaior}')
