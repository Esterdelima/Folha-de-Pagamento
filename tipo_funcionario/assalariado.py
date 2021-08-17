from modelo.funcionario_model import Funcionario

class Assalariado(Funcionario):

    salario = float
    valorComissao = float

    def __init__(self, nome, endereco, sindicato, id, taxaServico, salario, tipoFuncionario): #valorComissao
        super().__init__(nome, endereco, sindicato, id, taxaServico, tipoFuncionario)
        self.salario = salario
        #self.valorComissao = valorComissao


    def setSalario(self, salario):
        self.salario = salario

    # def setValorComissao(self, valorComissao):
        # self.valorComissao = valorComissao

    # def getValorComissao(self):
        # return self.valorComissao

    def getSalario(self):
        return self.salario

    # def comissao(self, salario, valorComissao):
    def salarioAssalariado(self, sindicato, taxaServico, salario):
        if sindicato > 0:
            if taxaServico > 0:
                return salario - sindicato - taxaServico
                
            else:
                return salario - sindicato
        else:
            return salario

    
