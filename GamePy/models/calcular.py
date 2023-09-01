from random import randint


class Calcular:

    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3) # 1 = somar, 2 = diminuir, 3 = multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:
            return 'Operacao desconhecida'

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operacao desconhecida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        if self.__dificuldade == 1:
            return randint(0, 10)
        elif self.__dificuldade == 2:
            return randint(11, 100)
        elif self.__dificuldade == 3:
            return randint(101, 1000)
        elif self.__dificuldade == 4:
            return randint(1001, 10000)
        else:
            return randint(10001, 1000000000)
    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.__valor1 + self.__valor2
        elif self.operacao == 2:
            return self.__valor1 - self.__valor2
        elif self.operacao == 3:
            return self.__valor1 * self.__valor2
        else:
            op = 'Operacao desconhecida'

    def checar_resultado(self: object, resposta: int) -> bool:
        if self.resultado == resposta:
            print('Resposta correta!')
            return True
        print(f'Voce perdeu 1 ponto, o resultado deveria ser: {self.resultado}')
        return False

    def mostrar_operacao(self: object) -> None:
        return f'{self.valor1} {self._op_simbolo} {self.valor2} = '

