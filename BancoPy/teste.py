'''
from Python_Projects.BancoPy.models.v1_calcular import ContaBanco
from typing import List, Dict

cc1 = ContaBanco('Joao', 11785978659, '123456')
cc2 = ContaBanco('Pedro', 987654321, '654321')
banco_de_contas: List[ContaBanco] = [cc1, cc2]

print(cc1)
cc1.depositar(1000)
print(cc1.saldo)
print(cc2.saldo)

cc1.trasferencia_conta_b(cc2, 50)
print(cc1.saldo)
print(cc2.saldo)
'''
from Python_Projects.BancoPy.models.v2_cliente import Cliente
from Python_Projects.BancoPy.models.v2_conta import Conta

felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-10', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '234.567.891-01', '08/07/1978')

# print(felicity)
# print(angelina)

contaf: Cliente = Conta(felicity)
contaa: Cliente = Conta(angelina)

print(contaf)
print(contaa)

