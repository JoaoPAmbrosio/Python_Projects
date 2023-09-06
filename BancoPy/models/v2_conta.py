from Python_Projects.BancoPy.models.v2_cliente import Cliente
from Python_Projects.BancoPy.utils.v2_helper import formata_float_str_moeda


class Conta:

    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return (f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} \n'
                f'Saldo total: {formata_float_str_moeda(self.saldo_total)}')

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    # Com o setter a mais torna possivel, nao somente buscar o valor com o property, mas enviar o valor, passando
    # novo valor limite do usuario

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        pass

    def sacar(self: object, valor: float) -> None:
        pass

    def transferir(self: object, destino: object, valor: float) -> None:
        pass

