from modelo.funcionario_model import Funcionario
#from salarioModel import Salario

class Comissario(Funcionario):

    taxaComissao = float


    def __init__(self, nome, endereco, sindicato, id, taxaServico, taxaComissao, tipoFuncionario):
        super().__init__(nome, endereco, sindicato, id, taxaServico, tipoFuncionario)
        self.taxaComissao = taxaComissao


    def setTaxaComissao(self, taxaComissao):
        self.taxaComissao = taxaComissao

    def getTaxaComissao(self):
        return self.taxaComissao

    def comissao(self, sindicato, taxaServico, taxaComissao):
        novoSalario = float
        if sindicato > 0:
            if taxaServico > 0:
                novoSalario = taxaComissao - sindicato - taxaServico
                return novoSalario
            else:
                novoSalario = taxaComissao - sindicato
            return novoSalario
        else:
            return taxaComissao

