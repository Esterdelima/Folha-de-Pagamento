from modelo.funcionario_model import Funcionario

class Assalariado(Funcionario):

    salario = float
    
    def __init__(self, nome, endereco, sindicato, salario):
        super().__init__(nome, endereco, sindicato)
        self.salario = salario

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario

    
