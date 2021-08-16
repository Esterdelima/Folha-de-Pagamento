
class Funcionario():
    nome = ''
    endereco = ''
    id = int
    sindicato = bool
    valorSalario = float

    def __init__(self, nome, endereco, sindicato, id):
        self.nome = nome
        self.endereco = endereco
        self.sindicato = sindicato
        self.id = id

    def toString(self):
        return 'Nome: ' + self.nome + ' | Endereço: ' + self.endereco +' | Sindicato: ' + str(self.sindicato) +' | Id: ' + str(self.id)

    def setNome(self, nome):
        self.nome = nome

    def setEndereco(self, endereco):
        self.endereco = endereco

    def setSindicato(self, sindicato):
        self.endereco = sindicato

    def setValorSalario(self, valorSalario):
        self.valorSalario = valorSalario

    def getValorSalario(self):
        return self.valorSalario

    def getNome(self):
        return self.nome

    def getEndereco(self):
        return self.endereco

    def getSindicato(self):
        return self.sindicato

    def getId(self):
        return self.id