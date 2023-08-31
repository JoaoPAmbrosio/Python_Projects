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
    print('')
    nome: str = input("Informe o nome do produto: ")
    preco: float = float(input('Informe o valor do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Lista de produtos')
        print('')
        [print(produto) for produto in produtos]
        # Faz com que o str de produto seja imprimido, com codigo numero e preco
        tempo = input('Aperte enter para sair')
        menu()
    else:
        print('Ainda nao existem produtos cadastrados.')
        sleep(2)
        menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Produtos disponíveis')
        [print(produto) for produto in produtos]
        print('Informe o codigo do produto que deseja adicionar ao carrinho: ')
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            # Se nao é None
            #Aqui fiz diferente
            no_carrinho: bool = False
            # Ja no carrinho
            for item in carrinho:
                # {{a: b}: unid}
                quant: int = item.get(produto)
                if quant > 0:
                    no_carrinho = True
                    item[produto] = quant + 1
                    print(f'O produto {produto.nome} agora possui { quant + 1} unidades no carrinho')
                '''
                for dados in item.items():
                    if dados[0] == produto:
                        n = dados[1]
                        dict[item] = {produto: n + 1}
                        print(f'O produto {dados[0].nome} agora possui {dados[1]} unidades no carrinho')
                        no_carrinho = True
                        print(dados)'''
            # Ainda nao no carrinho
            if no_carrinho is False:
                carrinho.append({produto: 1})
                print(f'O produto {produto.nome.title()} foi adicionado no carrinho!')
            sleep(2)
            menu()
        else:
            print(f'O produto com codigo {codigo} não foi encontrado!')
            sleep(2)
            menu()

    else:
        print('Ainda não existem produtos para vender. ')
        sleep(2)
        menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Vizualizar carrinho')
        print('')
        for item in carrinho:
            for dado in item.items():
                print(dado[0])
                print(f'Quantidade: {dado[1]}')
                print('------------------------')
    # car = [{{a, b}, unid}, {{a, b}, unid}]
    # {{a, b}, unid}
    else:
        print('Ainda nao possuem produtos no carrinho!')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        print('Fechar pedido')
        print('')
        valor_total: float = 0
        for item in carrinho:
            print(item[Produto])
            print(f'Quantidade: {item[1]}')
            valor_total += item[Produto.preco] * item[1]
        print(f'A sua fatura é {formata_float_str_moeda(valor_total)}')
        print(f'Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Carrinho vazio!')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ =='__main__':
    main()


