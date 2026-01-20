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


def atualizar_tarefa():
    pass    # Adicionar uma nova tarefa a lista já existente  (Atualizar/Editar)  ->  lista[i] = novo



def deletar_tarefa():
    pass   # Deletar item, deletar lista, deletar tudo. Botão de confirmação: "TEM CERTEZA QUE DESEJA DELETAR TUDO?" (Deletar/Remover)  ->  pop() ou remove()


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
