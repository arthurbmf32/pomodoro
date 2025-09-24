import time

def encontrar_tarefa(tarefa):
    return tarefa in lista_tarefas

def temporizador():
    tempo_em_segundos = 1500
    for i in range(1,6):
        if i < 5:
            tempo_em_segundos = 1500
            print(f"Pomodoro {i}: Iniciando...")
            while tempo_em_segundos:
                minutos, segundos = divmod(tempo_em_segundos, 60)
                timer = f'{minutos:02d}:{segundos:02d}'
                print(timer, end='\r')
                time.sleep(1)
                tempo_em_segundos -= 1
            print('PAUSA!')
        else:
            print(f"Pomodoro {i}: Iniciando...")
            while tempo_em_segundos:
                minutos, segundos = divmod(tempo_em_segundos, 60)
                timer = f'{minutos:02d}:{segundos:02d}'
                print(timer, end='\r')
                time.sleep(1)
                tempo_em_segundos -= 1
            print('PAUSA LONGA\nTérmino do ciclo de Pomodoro!')


lista_tarefas = []

while True:
    tarefa = str(input("Digite a tarefa a ser adicionada (ou 'sair' para encerrar): ").lower())
    if tarefa == 'sair':
        break
    else:
        lista_tarefas.append(tarefa)
    print("Tarefa adicionada:", tarefa)

tarefa_desejada = str(input("Digite a tarefa que você deseja realizar: ").lower())

while True:
    if encontrar_tarefa(tarefa_desejada):
        print("Tarefa encontrada! Iniciando o Pomodoro para a tarefa:", tarefa_desejada)
        temporizador()
        break
    else:
        print("Tarefa não encontrada na lista.")
        tarefa_desejada = str(input("Digite a tarefa que você deseja realizar: ").lower())

