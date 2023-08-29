"""
Math Game - Final version

This was the final version of a math game in portuguese.
The aim is to be a program using Python that can be used to train mathematical skills in an interactive way,
using points to reward sucess.
"""
from Python_Projects.GamePy.models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    niveis = [1, 2, 3, 4]
    while (dificuldade := int(input('Informe o nivel de difiduldade desejado [1, 2, 3 ou 4]: '))) not in niveis:
        print('Digite valor correto')

    calc: Calcular = Calcular(dificuldade)

    resultado: int = int(input(f'Informe o resultado para a seguinte operação:\n{calc.mostrar_operacao()}'))

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Voce tem {pontos} ponto(s).')
    else:
        pontos -= 1

    print(f'{calc.mostrar_operacao()} {calc.resultado}')

    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou com {pontos} ponto(s). ')
        print('Até a proxima!')


if __name__ == '__main__':
    main()
