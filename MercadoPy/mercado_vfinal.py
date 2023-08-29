from typing import List, Dict
from time import sleep

from Python_Projects.MercadoPy.models.produto import Produto
from Python_Projects.MercadoPy.utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('Mercado Ambrosio! \nAqui, temos de tudo e muito mais!')
    # [print(i['nome'].title(), end=', ') for i in dados_totais]
    print('')
    print('Digite:')
    print('1 -> Para cadastrar novo produto.')
    print('2 -> Ver lista com valores.')
    print('3 -> Comprar.')
    print('4 -> Visualizar o carrinho.')
    print('5 -> Concluir compra')
    print('0 -> Para sair')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 0:
        print('Volte sempre!')
        sleep(2)
        exit(1)
    else:
        print('Opção inválida!')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto')

def listar_produtos() -> None:
    pass

def comprar_produto() -> None:
    pass

def visualizar_carrinho() -> None:
    pass

def fechar_pedido() -> None:
    pass

def pega_produto_por_codigo(codigo: int) -> Produto:
    pass

if __name__ =='__main__':
    main()
