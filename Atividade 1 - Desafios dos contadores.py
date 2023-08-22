"""
Desafios dos contadores!
Faça um contador, que tenha uma estrutura de repetição, que conte crescente e decrescente!
"""
print('1º solução')

contador_decres = 10
contador_cresce = 0
for numero in range(0, 10):
    print(contador_cresce, contador_decres)
    contador_cresce += 1
    contador_decres -= 1

print('\n', '2º solução')

valores = list(range(0, 11))
for indices, valor in enumerate(valores, -10):
    indices *= -1
    print(valor, indices)

print('\n', '3º solução')

contador_decres = 10
contador_cresce = 0
while contador_cresce <= 10:
    print(contador_cresce, contador_decres)
    contador_cresce += 1
    contador_decres -= 1

print('\n', '4º solução')

for n in range(0, 10):
    print(f'\t{n}', end='')
print()
for v in range(10, 0, -1):
    print(f'\t{v}', end='')

print('\n\n', '5º solução')

Lista_1 = []
lista_2 = []
contador = 0
for num1 in range(0, 10):
    Lista_1.append(num1)
    for num2 in range(10, 0, -1):
        if num2 in lista_2:
            lista_2.pop()
        else:
            lista_2.append(num2)
while contador < 10:
    if contador % 2 == 0:
        print(Lista_1[contador], lista_2[contador])
        contador += 1
    else:
        print(Lista_1[contador], lista_2[contador])
        contador += 1
