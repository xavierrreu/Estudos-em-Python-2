'''
4)	Faça um programa que receba dez números e armazene em uma lista.
 Em seguida calcule a soma de todos os números percorrendo novamente a lista. Apresente a soma e em seguida a média baseada na soma e no número de números armazenados.
'''


lista = [0]*10
soma = 0
c = 0

for i in range(10):
    print('Digite um número')
    lista[i] = int(input())
    soma += lista[i]
    c+=1

media = soma/c
    

print (f"a soma é {soma}")
print(f'A média é: {media}')
