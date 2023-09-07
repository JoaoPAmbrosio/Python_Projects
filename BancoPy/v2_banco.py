"""
Bank - Version 2

This was the fist version of a bank program in portuguese.
The aim is to be a program that can be used to simulate an online bank, where the user can create an account and,
 with it, make different types of financial transactions as withdrawals, deposits, transfers, etc.
"""

from typing import List
from time import sleep
from Python_Projects.BancoPy.models.v2_cliente import Cliente
from Python_Projects.BancoPy.models.v2_conta import Conta


contas: List[Conta] = []

felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-10', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '234.567.891-01', '08/07/1978')
contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)
contas.append(contaf)
contas.append(contaa)

def main() -> None:
    menu()


def menu() -> None:
    print('==============================================')
    print('================   ATM   =====================')
    print('============== Ambrosio bank =================')
    print('==============================================')
    print('Selecione uma opção no menu:')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar deposito')
    print('4 - Efetuar transferencia')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao ==5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(6)
    else:
        print(f"Opção '{opcao}' inválida")
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')
    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta')
    print('-------------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
            # Nome do metodo é efetuar saque e nao sacar
            # Aqui nao tem regras de saldo, limite, que estao definidas na classe e nao no programa
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda nao existem contas cadastradas. ')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do deposito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda nao existem contas cadastradas. ')
    sleep(2)
    menu()

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))
        conta_o: Conta = buscar_conta_por_numero(numero_o)
        if conta_o:
            numero_d: int = int(input('Informe o número da conta de destino: '))
            conta_d: Conta = buscar_conta_por_numero(numero_d)
            if conta_d:
                valor: float = float(input('Informe o valor da tranferencia: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'Não foi encontrada a conta com número {numero_d}')
        else:
            print(f'Não foi encontrada a conta com número {numero_o}')
    else:
        print('Ainda nao existem contas cadastradas. ')
    sleep(2)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas:\n')
        [print(f'{conta}\n-------------------------------') for conta in contas]
    else:
        print('Ainda nao existem contas cadastradas. ')
    sleep(2)
    menu()

def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
