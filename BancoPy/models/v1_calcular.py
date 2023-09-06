
class ContaBanco:

    contador = 10000

    def __init__(self: object, nome: str, cpf: int, senha: str) -> None:
        self.__conta = ContaBanco.contador
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha
        self.__saldo = 0
        ContaBanco.contador += 1

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
    def senha(self: object) -> str:
        return self.__senha

    @property
    def saldo(self: object) -> int:
        return self.__saldo

    def depositar(self: object, valor: int) -> None:
        self.__saldo += valor

    def sacar(self: object, valor: int) -> None:
        self.__saldo -= valor

    # ainda entender
    def trasferencia_conta_b(self: object, conta_destino: object, valor: int) -> None:
        self.__saldo -= valor
        conta_destino.__saldo += valor

    def __str__(self) -> str:
        return (f'Abertura de conta realizada Sr(a) {self.nome}! \nNumero CC: {self.conta} \nSenha: {self.senha} '
                f'\nSaldo: {self.saldo}')
