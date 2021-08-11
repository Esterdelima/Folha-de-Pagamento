from modelo.funcionario_model import Funcionario

class Assalariado(Funcionario):

    salario = float
    
    def __init__(self, nome, endereco, sindicato, valorSalario, salario):
        super().__init__(nome, endereco, sindicato, valorSalario)
        self.salario = salario

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario
