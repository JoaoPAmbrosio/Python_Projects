"""
Market - Version 2 - Learning

This was the second version of a market program in portuguese.
The aim is to be a program that can be used to simulate an online market, where the user can choose items with
different quantities to add in a basket and in the end to buy them.
"""
from Python_Projects.MercadoPy.models.calcular_v2 import Mercado

dados_totais = [{'nome': 'abacaxi', 'valor': 3, 'quantidade': 0},
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

info_mercado = Mercado(dados_totais)

print('Mercado Ambrosio! \nAqui, temos de tudo:')
[print(i['nome'].title(), end=', ') for i in dados_totais]
print('e muito mais!')

tempo_de_espera = 5
mercado = True
while mercado:
    opcoes = [1, 2, 3, 4, 5, 0] # lista com valores, comprar, visualizar carrinho, cadastrar, sair
    while (x := int(input('\nDigite: \n1 -> Ver lista com valores.\n2 -> Visualizar o carrinho.\n3 -> Comprar.\n'
              '4 -> Concluir compra\n5 -> Para cadastrar novo produto.\n0 -> Para sair\nDigite o que deseja: '))) not in opcoes:
        print('Voce digitou um valor errado!')

    if x == 0:
        print('Compra cancelada! Muito obrigado e volte sempre!')
        mercado = False

    # 1 -> Ver lista com valores.
    elif x == 1:
        for item in info_mercado.banco_de_dados:
           print(f"{item['nome'].title()}: R$ {float(item['valor'])}", end=', ')
        enter = input('\nPrecione enter para seguir:')

    # 2 -> Visualizar o carrinho. (Melhorar!)
    elif x == 2:
        if len(info_mercado.carrinho) == 0:
            print('Carrinho vazio!')
        else:
            print('Visualização carrinho:')
            for i in info_mercado.carrinho:
                print(f"({i['quantidade']}) x {i['nome'].title()}(s) = R$ {i['valor']*i['quantidade']} | "
                      f"R$ {i['valor']}/kg")
            print(f'Soma valor parcial: R$ {float(info_mercado.soma_total_compra)}')
        enter = input('Precione enter para seguir:')

    # 3 -> Comprar.
    elif x == 3:
        while info_mercado.procurar_item(compra := input('Digite o que deseja comprar ou digite sair: ')) is False:
            if compra.lower() == 'sair':
                break
            print('Nao encontrada! Cadastre ou digite corretamente')
        if compra.lower() != 'sair':
            compra = compra.lower()

            # Verificar se ja tem um mesmo no carrinho e alterar
            qtd = 0
            for i in info_mercado.carrinho:
                if i['nome'] == compra:
                    print('Voce ja tem esta fruta no carrinho.')
                    qtd = int(input('Digite nova quantidade: '))
                    i['quantidade'] = qtd
            if qtd == 0:
                qtd = int(input('Digite a quantidade que deseja comprar: '))
                info_mercado.carrinho.append({'nome': compra, 'valor': info_mercado.procurar_valor(compra), 'quantidade': qtd})

    # 4 -> Concluir compra
    elif x == 4:
        valor_compra = info_mercado.soma_total_compra
        print(f'Valor total: R$ {float(valor_compra)} \nMuito obrigado pela preferencia!')
        mercado = False

    # 5 -> Para cadastrar novo produto.
    elif x == 5:
        compra = input('Digite o item que deseja cadastrar: ')
        if info_mercado.procurar_item(compra):
            print('Fruta ja cadastrada!')
        else:
            valor = int(input('Digite o valor do item: '))
            qtd = 0
            info_mercado.banco_de_dados.append({'nome': compra, 'valor': valor, 'quantidade': qtd})




