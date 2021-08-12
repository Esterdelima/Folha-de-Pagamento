from modelo.funcionario_model import Funcionario
from salario_model import Salario

class Horista(Funcionario):

    horas = int
    valorSalario = float

    def __init__(self, nome, endereco, sindicato, valorSalario, horas):
        super().__init__(nome, endereco, sindicato)
        self.horas = horas
        self.valorSalario = valorSalario

    def __init__(self, horas, valorSalario):
        self.horas = horas
        self.valorSalario = valorSalario
        
    
    def setHoras(self, horas):
        self.horas = horas

    def setValorSalario(self, valorSalario):
        self.valorSalario = valorSalario

    def getValorSalario(self):
        return self.valorSalario

    def getHoras(self):
        return self.horas


    def cartaoPonto(self, horas, valorSalario,valorSindicato):
        salario = float
        if horas > 8:
            extra = valorSalario * 1.5 * (horas-8)
            salario += (8 * valorSalario) + extra
    
        else :
            salario += horas * valorSalario
    
        return salario - valorSindicato
        