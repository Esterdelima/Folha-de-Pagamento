from modelo.funcionario_model import Funcionario
# from modelo.salario_model import Salario
# from tipo_funcionario.assalariado import Assalariado
# from tipo_funcionario.comissario import Comissario
# from tipo_funcionario.horista import Horista
from funcionalidades.crudFuncionario import CrudFuncionario
# 
# listaFuncionario = []
# listaTipoFuncionario = []

def opcoesFuncionario():
    print("\nOpções de funcionário:")
    print("""    1 - Adicionar funcionário
    2 - Remover funcionário
    3 - Lançamentos
    4 - Alterar dados
    5 - Listar funcionários
    6 - Voltar""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
        nome = input("Insira o nome do funcionario a ser adicionado:\n")
        endereco = input("Insira o endereço do funcionario a ser adicionado:\n")
        print("""Faz parte de sindicato:
        1 - Sim
        2 - Não""")
        sindicato = bool
        escolha = int(input())
        while escolha > 2:
            escolha = int(input("Não entendi, escolha novamente: "))
        if escolha == 1:
            sindicato = True
        else:
            sindicato = False

        funcionario = Funcionario(nome, endereco, sindicato)
        CrudFuncionario.criarFuncionario(funcionario)
        CrudFuncionario.listar()

        #opcoes()

opcoesFuncionario()

    # elif escolha == 2: #AINDA FALTA FAZER
        # listaFuncionario()
        # id = int(input("Insira o id do funcionário deseja demitir: "))
        # listaFuncionario.pop(id)
        # opcoes()

    # elif escolha == 3:
        # 
        # id = int(input("Insira o id do funcionário que fará o lançamento: "))
        # print("""Insira o tipo de lançamento:
        # 1 - Cartão de ponto
        # 2 - Venda
        # 3 - Serviço""")
        # escolha = int(input())
        # if escolha == 1:

            # horas = int(input("Insira a quantidade de horas trabalhadas: "))
            # valorSalario = float(input("Insira o salario por horas trabalhadas: "))
            # horista = Horista(horas, valorSalario)
            # if listaFuncionario.Sindica

        # elif escolha == 2:
            # funcionarios[id].venda()
        # elif escolha == 3:
            # funcionarios[id].servico()
        # opcoes()

    # elif escolha == 4:
        # listar()
        # id = int(input("Insira o id do funcionário desejado: "))
        # funcionarios[id].alterarDados()
        # opcoes()

    # elif escolha == 5:
        # listar()
        # opcoes()

    # elif escolha == 6:
        # opcoes()
        # 
    # else:
        # print("Não entendi, vamos recomeçar o atendimento")
        # opcoesFuncionario()


