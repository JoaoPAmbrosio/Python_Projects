from Python_Projects.BancoPy.models.calcular import ContaBanco
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
