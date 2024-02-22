"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de Pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de Print: {ret_pr}')

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None.

OBS: Funções Python que retornam valores, devem retornar estes valores com a
palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno
de uma função. Podemos passar a execução da função para outras funções.

# Vamos refatorar esta função para que ela retorne o valor.


def quadrado_de_7():
    return 7 * 7


# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7() + 1}')

# Refatorando a primeira função


def diz_oi():
    return 'Oi '


alguem = 'Thamiris!'

print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;


def diz_oi():
    print('Estou sendo executado, por favor, me ajude!')
    return 'Oi! '
    print('Estou sendo executado, por favor, me ajude!')


print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns;


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;


def outra_funcao():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)

print(outra_funcao())

"""

# Vamos criar uma função para jogar a moeda

from random import random
from random import randint
from time import sleep

# def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    # valor = random()
    # if valor > 0.5:
       # return 'Cara'
    # return 'Coroa'


# print(joga_moeda())

# Definindo itens
itens = ('Pedra', 'Papel', 'Tesoura')

# Jogada do computador
computador = randint(0, 2)

# Apresentar suas opções
print("""Suas opções :
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

# Agora o jogador faz a jogada...
jogador = int(input('Qual sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)
print('-=' * 11)

# Mostrando o que cada um jogou
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 11)

if computador == 0: #  Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')

    elif jogador ==1:
        print('JOGADOR VENCE')

    elif jogador ==2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador ==1: #  Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')

    elif jogador == 1:
         print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA')

elif computador ==2: #  Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCEU')

    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
