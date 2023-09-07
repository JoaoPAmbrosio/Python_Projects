"""
Market - Version 1 - Learning

This was the fist version of a market program in portuguese.
The aim is to be a program that can be used to simulate an online market, where the user can choose items with
different quantities to add in a basket and in the end to buy them.
"""
from unidecode import unidecode

lista_frutas = ['abacaxi', 'abacate', 'banana', 'coco', 'laranja', 'limão', 'mamão','manga', 'maçã', 'melancia',
                'melão', 'pera', 'pêssego', 'tangerina', 'uva']

banco_de_dados = [{'nome': 'abacaxi', 'valor': 3, 'quantidade': 0},
                  {'nome': 'abacate', 'valor': 2, 'quantidade': 0},
                  {'nome': 'banana', 'valor': 2.25, 'quantidade': 0},
                  {'nome': 'coco', 'valor': 2, 'quantidade': 0},
                  {'nome': 'laranja', 'valor': 1.8, 'quantidade': 0},
                  {'nome': 'limão', 'valor': 1.5, 'quantidade': 0},
                  {'nome': 'mamão', 'valor': 3.99,'quantidade': 0},
                  {'nome': 'manga', 'valor': 4.99, 'quantidade': 0},
                  {'nome': 'maçã', 'valor': 3.1, 'quantidade': 0},
                  {'nome': 'melancia', 'valor': 1.49, 'quantidade': 0},
                  {'nome': 'melão', 'valor': 2.7, 'quantidade': 0},
                  {'nome': 'pera', 'valor': 5.4,'quantidade': 0},
                  {'nome': 'pêssego', 'valor': 6.8,'quantidade': 0},
                  {'nome': 'tangerina', 'valor': 6.5, 'quantidade': 0},
                  {'nome': 'uva', 'valor': 7.7, 'quantidade': 0}]


def procurar_fruta(nome_fruta):
    for i in range(len(banco_de_dados)):
        if unidecode((banco_de_dados[i]['nome']).lower()) == unidecode(nome_fruta.lower()):
            return True
    return False


def procurar_valor(nome_fruta):
    for i in range(len(banco_de_dados)):
        if unidecode((banco_de_dados[i]['nome']).lower()) == unidecode(nome_fruta.lower()):
            return banco_de_dados[i]['valor']
    return f'Nao encontrado!'


def soma_total_compra(carrinho):
    if len(carrinho) == 0:
        return 0
    soma = 0
    for i in carrinho:
        soma = soma + i['valor'] * i['quantidade']
    return soma


print('Mercado de Frutas Ambrosio! \nAqui, temos de tudo:')
[print(i['nome'].title(), end= ', ') for i in banco_de_dados]
print('e muito mais!')

mercado = True
carrinho = []
while mercado:
    opcoes = [1, 2, 3, 4, 5, 0] # lista com valores, comprar, visualizar carrinho, cadastrar, sair
    while (x := int(input('Digite: \n1 -> Ver lista com valores.\n2 -> Comprar.\n3 -> Visualizar o carrinho.\n'
              '4 -> Para cadastrar novo produto.\n5 -> Concluir compra\n0 -> Para sair\nDigite o que deseja: '))) not in opcoes:
        print('Voce digitou um valor errado!')

    if x == 0:
        mercado = False
        print('Compra cancelada! Muito obrigado e volte sempre!')

    # 1 -> Ver lista com valores.
    elif x == 1:
        for fruta in banco_de_dados:
            print(f"{fruta['nome'].title()}: R$ {float(fruta['valor'])}", end=', ')

    # 2 -> Comprar.
    elif x == 2:
        while procurar_fruta(compra := input('Digite o que deseja comprar ou digite sair: ')) is False:
            if compra.lower() == 'sair':
                break
            print('Nao encontrada! Cadastre ou digite corretamente')
        if compra.lower() != 'sair':
            compra = compra.lower()

            # Verificar se ja tem um mesmo no carrinho e alterar
            qtd = 0
            for i in carrinho:
                if i['nome'] == compra:
                    print('Voce ja tem esta fruta no carrinho.')
                    qtd = int(input('Digite nova quantidade: '))
                    i['quantidade'] = qtd

            if qtd == 0:
                qtd = int(input('Digite a quantidade que deseja comprar: '))
                carrinho.append({'nome': compra, 'valor': procurar_valor(compra), 'quantidade': qtd})

    # 3 -> Visualizar o carrinho. (Melhorar!)
    elif x == 3:
        if len(carrinho) == 0:
            print('Carrinho vazio!')
        else:
            print('Visualização carrinho:')
            for i in carrinho:
                print(f"({i['quantidade']}) x {i['nome'].title()}(s) = R$ {i['valor']*i['quantidade']} | "
                      f"R$ {i['valor']}/kg")
            print(f'Soma valor parcial: R$ {float(soma_total_compra(carrinho))}')

    # 4 -> Para cadastrar novo produto.
    elif x == 4:
        compra = input('Digite a fruta que deseja cadastrar: ')
        if procurar_fruta(compra):
            print('Fruta ja cadastrada!')
        else:
            valor = int(input('Digite o valor da fruta: '))
            qtd = 0
            banco_de_dados.append({'nome': compra, 'valor': valor, 'quantidade': qtd})

    # 5 -> Concluir compra
    elif x == 5:
        valor_compra = soma_total_compra(carrinho)
        print(f'Valor total: R$ {float(valor_compra)} \nMuito obrigado pela preferencia!')
        mercado = False
