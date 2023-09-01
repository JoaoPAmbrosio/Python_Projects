from Python_Projects.BancoPy.models.calcular import Banco

cc1 = Banco('Joao', 11785978659)
print(cc1)
cc1.depositar(1000)
print(cc1.saldo)