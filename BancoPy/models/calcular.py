
class Banco:

    contador = 10000

    def __init__(self: object, nome: str, cpf: int) -> None:
        self.__conta = Banco.contador
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = 0
        Banco.contador += 1

    @property
    def conta(self: object) -> int:
        return self.__conta

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self: object) -> int:
        return self.__cpf

    @property
    def saldo(self: object) -> int:
        return self.__saldo

    def depositar(self: object, valor: int) -> None:
        self.__saldo += valor

    def sacar(self: object, valor: int) -> None:
        self.__saldo -= valor

    # ainda entender
    def trasferencia_conta_b(self: object, conta_b: int, valor: int) -> None:
        self.__saldo -= valor

    def __str__(self) -> str:
        return (f'Abertura de conta realizada Sr(a) {self.nome}! \nNumero de conta: {self.conta} \nCpf: {self.cpf}'
                f'\nSaldo: {self.saldo}')
