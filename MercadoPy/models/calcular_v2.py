from unidecode import unidecode
class Mercado:

    def __init__(self, banco_de_dados):
        self.__banco_de_dados = banco_de_dados
        self.__carrinho = []
        self.__comprar = self
        self.__concluir_compra = self
        self.__sair = self


    @property
    def banco_de_dados(self):
        return self.__banco_de_dados

    @property
    def carrinho(self):
        return self.__carrinho

    def procurar_item(self, nome_item: str) -> bool:
        for i in range(len(self.banco_de_dados)):
            if unidecode((self.banco_de_dados[i]['nome']).lower()) == unidecode(nome_item.lower()):
                return True
        return False

    def procurar_valor(self, nome_item: str) -> int:
        for i in range(len(self.banco_de_dados)):
            if unidecode((self.banco_de_dados[i]['nome']).lower()) == unidecode(nome_item.lower()):
                return self.banco_de_dados[i]['valor']
        return 0

    @property
    def soma_total_compra(self) -> int:
        if len(self.carrinho) == 0:
            return 0
        soma = 0
        for i in self.carrinho:
            soma = soma + i['valor'] * i['quantidade']
        return soma


