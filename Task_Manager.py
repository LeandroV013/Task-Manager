# CRUD Create, Read, Update and Delete.
tarefas = []


def linha():
    print('-'*10)


def criar_tarefa():
    while True:
        resposta = input('Deseja criar uma nova tarefa? [S/N]: ').lower()

        if resposta == 's':
            nova_tarefa = input('Adicione uma nova tarefa: ')
            tarefas.append(nova_tarefa)
        elif resposta == 'n':
             break
        else:
            print('ENTRADA INVÁLIDA. DIGITE [S/N].')


def listar_tarefas(): # Adicionar enumerate
    if not tarefas:
        print('Você não tem nenhuma tarefa. ')
    else:
        print(tarefas)


def atualizar_tarefa():  # TRATAR ERRO DE STRING,CASO O USUÁRIO NÃO COLOQUE O NÚMERO, O CÓDIGO QUEBRA E VAI DAR ERRO DE ENTRADA
    if not tarefas:
         print('Você não tem nenhuma tarefa.')
    else:
        print('Suas tarefas: ')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}, {tarefa}')
        
        indice = int(input('Digite o número da tarefa que deseja editar: '))
        
        if indice < 1 or indice > len(tarefas):
            print('Número inválido.')
        else:
            nova_tarefa = input('Digite uma nova tarefa: ')
            tarefas[indice - 1] = nova_tarefa
            print('Tarefa atualizada com sucesso!')


def deletar_tarefa(): # DELETAR MAIS DE UMA TAREFA POR VEZ QUEBRA O CÓDIGO. COLOCAR OPÇÃO DE DELETAR MAIS DE UM OU DELETAR TUDO.
    if not tarefas:
        print('Você não pode apagar porque ainda não tem nenhuma tarefa.')
    else:
        print('Suas tarefas: ')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}, {tarefa}')

        indice = int(input('Digite o número da tarefa que deseja deletar: '))
        confirmacao = input(f'Tem certeza que deseja removar a tarefa "{indice}" [S/N]? ').lower()
        if confirmacao == 's':
            if indice < 1 or indice > len(tarefas):
                print('Número inválido.')
            else:
                tarefa_removida = tarefas.pop(indice - 1)
                print(f'Tarefa "{tarefa_removida}" removida com sucesso!')



def menu(): # Mostrar opções e criar funções, nada além disso
        return input(f'Gerenciador de Tarefas \nSelecione uma opção: [C]riar, [L]istar, [A]tualizar, [D]eletar, [M]enu: ')


while True:
    select = menu().lower()
    if not select or select[0] not in 'cladm':
        print('Selecione uma opção válida. ')
        continue
     
    elif select[0].lower() == 'c':
         criar_tarefa()


    elif select[0].lower() == 'l':
         listar_tarefas()


    elif select[0].lower() == 'a':
         atualizar_tarefa()


    elif select[0].lower() == 'd':
         deletar_tarefa()
