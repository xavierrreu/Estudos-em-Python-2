'''
7	Faça um programa que receba dez números e armazene em uma lista. 
Em seguida copie todos os números da primeira lista para uma segunda lista, mas na ordem invertida da primeira lista.
'''

lista1 = [0]*10
lista2 = [0]*10

for i in range(10):
    print('digite um número')
    lista1[i] = int(input())

# lista2 = lista1[::-1]
# print(lista1)
# print(lista2)

#ou...

destino = 9
for origem in range(10):
    lista2[destino] = lista1[origem]
    destino-=1


print(lista1)
print(lista2)
