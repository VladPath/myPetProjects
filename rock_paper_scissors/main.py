from random import choice, randint
from sys import exit

NAME = 'Человек'
FAIRNESS = 30
GAME_NAME = "Камень, ножницы и бумага "

if len(GAME_NAME) > 37:
    print("Очень длинное название игры ")
    exit()

num = (39 - len(GAME_NAME)) // 2

if len(GAME_NAME) % 2 == 0:
    x = 1
else:
    x = 0

print('* ' * 20 + '*')
print('*' + ' ' * 39 + '*')
print('*' +' ' * num + GAME_NAME + ' ' * (num + x) + '*')
print('* ', '  ' * 18, '*')
print('* ' * 21 ,)

gender_ending = ''
game = True
player_score = 0
computer_score = 0
rounds = 0
max_rounds = 0
win = ''

player_name = input("Привет, как тебя зовут? \n")
if player_name == '':
    player_name = NAME

print(f"\nПриветствую тебя {player_name.title()} в игре \"Камень, ножницы бумага\"")
print("\nПравила этой игры крайне просты")
print("камень побеждает ножницы")
print("ножницы побеждают бумагу")
print("и бумага побеждает камень")
print("\nда прибудет с вами сила!!")

print(f"\n{player_name.title()} выбери уровень сложности: ")
print("1 - Стандартный уровень")
print("2 - Сложный уровень")
print("3 - Невероятный уровень")

player_level = input()
while player_level not in ['1', '2', '3']:
    player_level = input("Просто введи цифру 1, 2 или 3\n")

print(f"\n{player_name} выбери количество раундов от 1 до бесконечности (0 - бесконечное колличество раундов) ")
player_round = input()

while not player_round.isdigit() or int(player_round) < 0:
    player_round = input("Просто введи число от 1 до бесконечности (0 - для бесконечности) ")
if player_round == '0':
    max_rounds = 9999
else:
    max_rounds = player_round
while game and rounds < int(max_rounds):
    if player_level == '1':
        computer_option = choice(['камень', 'ножницы', 'бумага'])
    elif player_level == '2':
        if rounds == 0:
            computer_option = choice(['камень', 'ножницы', 'бумага'])
        else:
            if player_option == 'камень' and win == 'player':
                computer_option = 'бумага'
            elif player_option == 'бумага' and win == 'player':
                computer_option = 'ножницы'
            elif player_option == 'ножницы' and win == 'player':
                computer_option = 'бумага'

            elif player_option == 'камень' and win == 'computer':
                computer_option = 'камень'
            elif player_option == 'бумага' and win == 'computer':
                computer_option = 'бумага'
            elif player_option == 'ножницы' and win == 'computer':
                computer_option = 'ножницы'
            else:
                computer_option = choice(['камень', 'ножницы', 'бумага'])




    player_option = input("\nКамень, ножницы, бумага или выход? ").lower()
    player_option_legal = ['камень', 'ножницы', 'бумага', 'выход']
    while player_option not in player_option_legal:
        print(f"{player_name}, {player_option} - это не легальная опция ")
        player_option = input("Выбери из камня, ножниц, бумаги или выхода: ").lower()

    if player_level == '3' and randint(1, 100) > FAIRNESS:
        if player_option == 'камень':
            computer_option = 'бумага'
        elif player_option == 'ножницы':
            computer_option = 'камень'
        else:
            computer_option = 'ножницы'

    if player_option == 'выход':
        print("Конец игры")
        game = False
    elif player_option == computer_option:
        print(f"\n{player_option} - выбор {player_name}, {computer_option} - выбор компьютера ")
        print("Ничья")

        rounds += 1


    elif (player_option == 'камень' and computer_option == 'ножницы' or
          player_option == 'ножницы' and computer_option == 'бумага' or
          player_option == 'бумага' and computer_option == 'камень'):
        print(f"{player_option} - выбор {player_name.title()}, {computer_option} - выбор компьютера ")
        print(f'выиграл {player_name.title()}')

        rounds += 1
        player_score += 1
        win = 'player'

    else:
        print(f"{player_option} - выбор {player_name.title()}, {computer_option} - выбор компьютера ")
        print("Выиграл компьютер")

        computer_score += 1
        rounds += 1
        win = 'computer'


print(f"\n{player_name.title()}, Вы сыграли {rounds} раундов")
print(f"{player_name.title()}, твое колличество очков - {player_score} , колличество очков у компьютера - {computer_score}!")

if player_score > computer_score:
    print(f"Поздравляю {player_name.title()}, ты победил!")
elif computer_score > player_score:
    print(f"К сожалению {player_name.title()}, ты проиграл")
else:
    print("Ничья, победила дружба!")



