'''
Faça um programa que carregue dois vetores, X e Y, com dez números inteiros cada um. Considere que os números de cada vetor digital, X e Y, não podem estar repetidos. 
Calcule e mostre os seguintes vetores resultantes:
a.	a união de X com Y (todos os elementos de X e os elementos de Y que não estejam em X)
b.	a diferença entre X e Y (todos os elementos de X que não existam em Y)
c.	a soma entre X e Y (soma de cada elemento de X com o elemento de mesma posição em Y)
d.	produto entre X e Y (multiplicação de cada elemento de X com o elemento de mesma posição em Y)
e.	a interseção entre X e Y (apenas os elementos que aparecem nos dois vetores)

'''

# montando conjunto X
x = [0]*10

for i in range(10):
    while True:
        achei = False #variável chamada de FLAG
        print("Digite um número (conjunto X): ")
        n = int(input())
        for j in range (10):
            if n == x[j]:
                achei = True
                break
        if achei:
            print('Número duplicado, digite novamente.')
        else:
            x[i] = n
            break
        
#montando conjunto Y

y = [0]*10

for i in range(10):
    while True:
        achei = False #variável chamada de FLAG
        print("Digite um número (conjunto Y): ")
        n1 = int(input())
        for j in range (10):
            if n1 == y [j]:
                achei = True
                break
        if achei:
            print('Número duplicado, digite novamente.')
        else:
            y[i] = n1
            break

print(f'O conjunto X sera igual a: {x}')
print(f'O conjunto Y sera igual a: {y}')

# Montando a UNIÂO de X com Y

uniao = [0]*20
for i in range(10):
    while True:
        dup = False
        uniao[i] = x[i]
        # print('cheguei aqui')
        for j in range(10):
            if y[i] == x[j]:
                dup = True
                break
        if dup:
            print(f'O número {y[i]} já existe no conjunto X. Não será adicionado à união.')
            break
        else:
            uniao[i+10] = y[i]
            break        

print(f'O conjunto união sera: {uniao}')

# Montando a DIFERENÇA de X e Y

dif =  [0]*10

proxlivre = 0
for i in range (10):
    while True:
        rep = False #flag
        for j in range (10):
            if x[i] == y[j]:
                rep = True
                break
        if rep:
            print(f'O numero {x[i]} ja existe no conjunto Y. Não fara parte do conjunto diferença!')
            break
        else:
            dif[proxlivre] = x[i]  
            proxlivre +=1     
            break

print(f'O conjunto da diferença de X em Y sera: {dif} ')   

#a soma entre X e Y (soma de cada elemento de X com o elemento de mesma posição em Y)

soma =  [0]*10
for i in range(10):
    soma[i] = (x[i] + y[i])

print(f'Soma entre o numero X e Y nas mesmas posicoes sera: {soma}')    

#d.	produto entre X e Y (multiplicação de cada elemento de X com o elemento de mesma posição em Y)

mult =  [0]*10
for i in range(10):
    mult[i] = (x[i] *y[i])

print(f'Multiplicação entre o numero X e Y nas mesmas posicoes sera: {mult}')  

#e.	a interseção entre X e Y (apenas os elementos que aparecem nos dois vetores)

inter = [0]*10
proxlivre = 0
for i in range(10):
    while True:
        rep = False
        for j in range(10):
            if x[i] == y[j]:
                rep =  True
                break
        if rep:
            inter[proxlivre] = x[i]
            proxlivre += 1
            break
        else:
            print('Não ha numeros repetidos entre os conjuntos X e Y.')
            break

print(f'O conjunto intercecção sera: {inter} ')
