import json
tarefas = []

def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas,arquivo)
        print("Tarefas salvas com sucesso!")


def carregar_tarefas():
    try:
        with open("tarefas.json", 'r') as arquivo:
            tarefas = json.load(arquivo)
            print("Tarefas carregadas com sucesso!")
            return tarefas
    except:
        print("Nenhum arquivo de tarefas encontrado! Começando uma nova lista.")
        return []



def adicionar_tarefa(nome,prioridade):
    tarefa = {  
            'nome': nome,
            'prioridade': prioridade
        }

    tarefas.append(tarefa)
    print("Tarefa adicionada!", tarefa)


def listar_tarefa():
    print("Lista de tarefas:")
    for tarefa in tarefas:
        print(f"- {tarefa['nome']} (prioridade {tarefa ['prioridade']})")


def remover_tarefas(nome):
    for tarefa in tarefas:
        if tarefa['nome'] == nome:
            tarefas.remove(tarefa)
            print("Tarefa removida:", nome)
            break
        else:
            print("Tarefa não encontrada!")

tarefas = carregar_tarefas()

while True:
    print("\n** Menu de Opções **")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Salvar")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    # Adicionar tarefa
    if opcao == '1':
        nome = input("Digite o nome da tarefa: ")
        prioridade = input("Digite a prioridade da tarefa: ")

        #função adicionar
        adicionar_tarefa(nome,prioridade)

    # Listar tarefas
    elif opcao == '2':
        listar_tarefa()

    # Remover tarefa
    elif opcao == '3':
        nome = input("Digite o nome da tarefa a ser removida:")
        remover_tarefas(nome)
    
    #salvar
    elif opcao == '4':
        salvar_tarefas()
    
    # Sair
    elif opcao == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
