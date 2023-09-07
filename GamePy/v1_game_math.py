"""
Math Game - Version 1 - Learning

This was the fist version of a math game in portuguese.
The aim is to be a program that can be used to train mathematical skills in an interactive way,
using points to reward sucess.
"""
from random import choice, randint
from unidecode import unidecode


def somar(a: int, b: int) -> int:
    return a + b


def diminuir(a: int, b: int) -> int:
    return a - b


def multiplicar(a: int, b: int) -> int:
    return a * b


def operacao(a: int, b: int) -> list[str, int]:
    oper = choice(('somar', 'diminuir', 'multiplicar'))
    if oper == 'somar':
        resul_oper = somar(a, b)
    elif oper == 'diminuir':
        resul_oper = diminuir(a, b)
    elif oper == 'multiplicar':
        resul_oper = multiplicar(a, b)
    return [oper, resul_oper]


def numero_aleatorio(x: str) -> int:
    if x == 'facil':
        return randint(0, 9)
    elif x == 'medio':
        return randint(10, 99)
    elif x == 'dificil':
        return randint(100, 999)

pontos = 0

while (x := (unidecode((nivel := input("Escolha o nível de dificuldade do jogo (fácil, médio ou difícil) ou 'sair': "))
                               .lower()))) not in ['facil', 'medio', 'dificil', 'sair']:
    print('voce digitou algo errado!')
clear = lambda: os.system('cls') or None
print(f'Nivel: {x.title()}')
if x == 'sair':
    quit(1)

while pontos >= 0:
    num01 = numero_aleatorio(x)
    num02 = numero_aleatorio(x)
    opr01 = operacao(num01, num02)
    y = int(input(f"Qual valor para '{opr01[0]}' '{num01}' por '{num02}': "))
    if y == opr01[1]:
        pontos += 1
        print('Boa!', end=' ')
    else:
        pontos -= 1
        print(f'Resposta correta: {opr01[1]}.')
    if pontos >= 0:
        print(f'Voce possui {pontos} ponto(s)!')
    else:
        print('Voce ficou sem pontos, mas obrigado por jogar o jogo!')

    # in case, the pearson wants to replay, it keeps the while working retoring the points:
    while (ret := (unidecode((j := input("Voce quer jogar novamente? 'sim' ou 'não' ")).lower()))) not in ['sim', 'nao']:
        print('voce digitou algo errado!')
    if ret == 'nao':
        break
    elif pontos < 0:
        pontos = 0
