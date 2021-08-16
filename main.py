from modelo.funcionario_model import Funcionario
# from modelo.salario_model import Salario
# from tipo_funcionario.assalariado import Assalariado
# from tipo_funcionario.comissario import Comissario
# from tipo_funcionario.horista import Horista
from funcionalidades.crudFuncionario import CrudFuncionario
# 
# listaFuncionario = []
# listaTipoFuncionario = []
crud = CrudFuncionario()

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
        novoId = int(crud.prefixo+str(crud.id))
        funcionario = Funcionario(nome, endereco, sindicato, novoId)
        crud.criarFuncionario(funcionario)
        crud.listar()
        input('\nPressione ENTER para continuar...')

        #opcoes()

    elif escolha == 2: #AINDA FALTA FAZER
        crud.listar()
        id = input('Informe o Id do funcionario que deseja remover: ')
        crud.remove(id)      

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

    elif escolha == 4:
        crud.listar()
        id = int(input("Insira o id do funcionário desejado: "))
        escolha = input("""Informe o dado que deseja alterar: 
                        1 - Nome
                        2 - Endereço
                        3 - Sindicato\n""")
        crud.editar(id, int(escolha))

    elif escolha == 5:
        crud.listar()
    

    elif escolha == 6:
        opcoes()
        # 
    # else:
        # print("Não entendi, vamos recomeçar o atendimento")
        # opcoesFuncionario()





def opcoes():
    print("\nMenu principal:")
    print("""    1 - Espaço funcionario
    2 - Folha de Pagamento
    3 - Sair""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
        opcoesFuncionario()
    elif escolha == 2:
        print("entra")
        #opcoesFolha()
    elif escolha == 3:
        print("Obrigada por utilizar nosso sistema, volte sempre!")
        return
    else:
        print("\nNão entendi, vamos recomeçar o atendimento")
        opcoes()

print("Seja bem-vindo ao sistema Folha de Pagamento")

opcoes()