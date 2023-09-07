"""
Bank - Version 1

This was the fist version of a bank program in portuguese.
The aim is to be a program that can be used to simulate an online bank, where the user can create an account and,
 with it, make different types of financial transactions as withdrawals, deposits, transfers, etc.
"""
from Python_Projects.BancoPy.models.v1_calcular import ContaBanco
from typing import List
from time import sleep

cc1 = ContaBanco('Joao', 11785978659, '123456')
cc2 = ContaBanco('Pedro', 987654321, '654321')
banco_de_contas: List[ContaBanco] = []
banco_de_contas.append(cc1)
banco_de_contas.append(cc2)


def main() -> None:
    menu()


def menu() -> None:
    print('Bem vindo ao Banco Ambrosio\n'
          'Digite 1 - Para criar nova conta ao Banco\n'
          'Digite 2 - Se já possui conta ao Banco\n'
          'Digite 0 - Para sair')
    print('O que deseja?')
    opcao = int(input())
    if opcao == 0:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    elif opcao == 1:
        criar_conta()
        sleep(2)
    elif opcao == 2:
        logar()
    else:
        print(f"A opção escolhida '{opcao}' não foi identificada, tente novamente!")
        sleep(2)
    main()


def menu_2() -> None:
    print('Digite a operação que deseja fazer: ')
    print('Digite 1 - Extrato\n'
          'Digite 2 - Efetuar Saque\n'
          'Digite 3 - Efetuar Deposito\n'
          'Digite 4 - Efetuar Transferencia\n'
          'Digite 0 - Retornar ao menu')


def criar_conta() -> None:
    nome: str = input('Digite o nome: ')
    cpf: int = int(input('Digite CPF: '))
    senha: str = input('Digite sua senha: ')
    ccx = ContaBanco(nome, cpf, senha)
    banco_de_contas.append(ccx)
    print(ccx)


def logar() -> None:
    logado = False
    while logado is not True:
        if len(banco_de_contas) > 0:
            conta_in: int = int(input('Digite a conta: '))
            senha_in: str = input("Digite a senha: ")
            for primaria in banco_de_contas:
                if primaria.conta == conta_in and primaria.senha == senha_in:
                    logado = True
                    while logado is True:
                        print(f'Bem vindo Sr(a) {primaria.nome}')
                        menu_2()
                        segunda_opcao = int(input())
                        if segunda_opcao == 0:
                            print('Voltando ao menu..')
                            logado = False
                            sleep(2)
                            menu()
                        elif segunda_opcao == 1:
                            extrato(primaria)
                            tempo_de_espera = input("Aperte 'enter' se deseja sair: ")
                        elif segunda_opcao == 2:
                            # (2) - efetuar saque
                            valor: int = int(input('Digite o valor que deseja sacar: '))
                            if primaria.saldo >= valor:
                                saque(primaria, valor)
                            else:
                                print(f'Saldo insuficiente! \nVoce possui R$ {float(primaria.saldo)} , em conta.')
                        elif segunda_opcao == 3:
                            # (3) - efetuar deposito
                            valor: int = int(input('Digite o valor que deseja depositar: '))
                            if valor > 0:
                                deposito(primaria, valor)
                            else:
                                print(f'Nao é possivel depositar o valor: {float(valor)}, em conta.')
                        elif segunda_opcao == 4:
                            # Descobrir se a conta ta certa, descobrir se possui valor
                            conta_destino = int(input('Digite a conta que deseja realizar a transferência: '))
                            for secundaria in banco_de_contas:
                                if secundaria.conta == conta_destino:
                                    while (val2 := int(input('Digite o valor a ser transferido: '))) > primaria.saldo:
                                        print(f'Saldo insuficiente! Voce possui R$ {float(primaria.saldo)} disponível.')
                                    transferencia(primaria, val2, secundaria)
            print('Senha ou usuario invalidos!')
            sleep(2)
        else:
            print('Nao existe contas cadastradas!')
            sleep(2)
            menu()


def extrato(cc: ContaBanco) -> None:
    print(f'R$ {float(cc.saldo)}')


def saque(cc: ContaBanco, valor: int) -> None:
    cc.sacar(valor)
    print(f'Valor sacado: {valor}\nNovo saldo: {cc.saldo}')


def deposito(cc: ContaBanco, valor: int) -> None:
    cc.depositar(valor)
    print(f'Valor depositado: {valor}\nNovo saldo: {cc.saldo}')


def transferencia(cc: ContaBanco, valor: int, conta_destino) -> None:
    cc.trasferencia_conta_b(conta_destino, valor)
    print(f'Transferencia de R$ {float(valor)} , realizada à conta {conta_destino.conta}.\n'
          f'Novo saldo em conta: R$ {float(cc.saldo)}.')


if __name__ == '__main__':
    menu()


