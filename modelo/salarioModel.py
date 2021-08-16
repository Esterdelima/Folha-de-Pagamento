
from _typeshed import Self


class Salario():
    
    dinheiro = float
    dataVencimento = ''

    def __init__(self, dinheiro, dataVencimento):
        self.dinheiro = dinheiro
        self.dataVencimento = dataVencimento

    def setDinheiro(self, dinheiro):
        self.dinheiro = dinheiro

    def setDataVencimento(self, dataVencimento):
        self.dataVencimento = dataVencimento

    def getDinheiro(self, dinheiro):
        self.dinheiro = dinheiro

    def getDataVencimento(self, dataVencimento):
        self.dataVencimento = dataVencimento
        

