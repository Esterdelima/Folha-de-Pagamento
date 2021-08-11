from modelo.funcionario_model import Funcionario

class Horista(Funcionario):

    hora = int

    def __init__(self, nome, endereco, sindicato, valorSalario, hora):
        super().__init__(nome, endereco, sindicato, valorSalario)
        self.hora = hora
    
    
    def setHora(self, hora):
        self.hora = hora

    def getHora(self):
        return self.hora