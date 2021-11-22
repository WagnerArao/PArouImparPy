from random import randint
cont = 0

print('=' * 50)
print('    VAMOS JOGAR PAR OU IMPAR?    ')
print('=' * 50)
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()
    comp = randint(1, 5)
    soma = n + comp
    print(f'Você jogou {n} e o computador jogou {comp}. Total de {soma}.', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if pi == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            print('=-' * 20)
            print(f'Você venceu {cont} vezes!')
            break
    if pi == 'I':
        if soma % 2 != 0:
            print('VOCÊ VENCEU!!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            print('=-' * 20)
            print(f'Você venceu {cont} vezes')
            break
