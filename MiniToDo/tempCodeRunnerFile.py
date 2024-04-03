
while flag == True:
    print(""" Ты в главном меню, ты можешь: добавить задание, удалить задание, посмотреть все задания, и посмотреть задания на час
введи что именно ты хочешь сделать:
          """
)
    print('Если ты хочешь остановить программу введи "exit"')
    next = input()
    
    if next == 'добавить задание':
        print("Введи час в котором ты хочешь выполнить задание и само задание")
        h = int(input()) 
        do = input()
        my_todo.__add__(h, do)
        print()
    
    elif next == 'удалить задание':
        print('В каком часу ты хочешь удалить задание?')
        h = int(input())

        print('Выбери номер задания которое ты хочешь удалить!')
        my_todo.__show_all_to_do_list__()
        key = int(input())
        
        my_todo.__dell_do__(h, key)
        print('Задание удалено')
        print()
    
    elif next == 'посмотреть все задания':
        my_todo.__show_all_to_do_list__()
        print()
        
    
    elif next == 'посмотреть задания на час':
        print('На какой час ты хочешь посмотреть задание')
        h = int(input())
        my_todo.__show_hour_to_do__(h)
        print()
    
    elif next == 'exit'