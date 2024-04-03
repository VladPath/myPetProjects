class toDay:
    t = {}
    for i in range(24):
        t[i]=[]
    
    def __init__(self) -> None:
        pass
    
    def __add__(self,h, do):
        if not self.t[h]:
            self.t[h] = {1:do}
        else:
            k = self.__get_last_key__(h)
            self.t[h][k+1] = do
    
    def __get_last_key__(self, h):
        for k,v in self.t[h].items():
            pass
        return k

    
    def __show_all_to_do_list__(self):
        for i in range(len(self.t)):
            if self.t[i]:
                for k,v in self.t[i].items():
                    print(f'Задача № {k}:В {i} часов дня {v}')
        
    
    def __show_hour_to_do__(self,h):
        if self.t[h]:
            for k,v in self.t[h].items():
                print(f'Задача № {k}:В {h} часов дня {v}')
                
    def __dell_do__(self, h, key):
        try:
            self.t[h][key]
            print('Задание удалено')

        except:
            print("Такого задания нет!")
        else:
            del self.t[h][key]
            
    
    
print('Привет дорогой друг это твой персональный ToDoList под названием "ToDay"')   
my_todo = toDay()

my_todo.__dell_do__


flag = True
while flag == True:
    print()
    print(""" Ты в главном меню, ты можешь: добавить задание, удалить задание, посмотреть все задания, и посмотреть задания на час
введи что именно ты хочешь сделать:
          """
)
    print('Если ты хочешь остановить программу введи "exit"')
    next = input()
    print()
    
    if next == 'добавить задание':
        print("Введи час в котором ты хочешь выполнить задание и само задание")
        h = int(input()) 
        do = input()
        my_todo.__add__(h, do)
        my_todo.__show_hour_to_do__(h)
        print()
        input()
    

    elif next == 'удалить задание':
        print('В каком часу ты хочешь удалить задание?')
        print()
        my_todo.__show_all_to_do_list__()
        h = int(input())


        print('Выбери номер задания которое ты хочешь удалить!')
        print('Выбери номер задания которое ты хочешь удалить!')
        key = int(input())
        
        my_todo.__dell_do__(h, key)
        print()
        input()
    
    elif next == 'посмотреть все задания':
        my_todo.__show_all_to_do_list__()
        print()
        input()
        
    
    elif next == 'посмотреть задания на час':
        print('На какой час ты хочешь посмотреть задание')
        h = int(input())
        my_todo.__show_hour_to_do__(h)
        print()
        input()
    
    elif next == 'exit':
        flag = False
    
        
    

    

    
# t = {}
# for i in range(24):
#     t[i]= []


# t[6] = {1:'Выгулять собаку'}
# t[6][2] = 'Пойти в школу'


# try: 
#     t[6][3]

# except:
#     print('такого нет')
# else:
#     print('такой есть')


# for k,v in t[6].items():
#     pass
# print(k)

# for k,v in t[6].items():
#     print(v)


# del t[6][1]
        
# print(t)




# a = [{1:'hello'},{2:'World'}]
# b = {1:'hello'}
# b[2] = 'helloo'