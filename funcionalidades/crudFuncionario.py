from modelo.funcionario_model import Funcionario

class CrudFuncionario:

    listaFuncionario = []
    
    def criarFuncionario(self, funcionario):
        self.listaFuncionario.append(funcionario)

    def listar(self):
        for f in self.listaFuncionario: 
            print(f.nome, f.endereco, f.sindicato)
        
