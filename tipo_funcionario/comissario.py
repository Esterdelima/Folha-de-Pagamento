from modelo.funcionario_model import Funcionario

class Comissario(Funcionario):

    taxaComissao = float

    def __init__(self, nome, endereco, sindicato, taxaComissao):
        super().__init__(nome, endereco, sindicato)
        self.taxaComissao = taxaComissao





