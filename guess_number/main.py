from random import randint
from sys import exit

MAXIMUM_NUMBER = 1000
GAME_NAME = "Угадай число"

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
total_attempts = 0
games = 0
gender_ending = ''

name = input("Как вас зовут? ")
if not name:
    name = 'Инкогнито'
gender = input("Введите ваш пол (м/ж) ")
while gender != 'м' and gender != 'ж':
    gender = input("просто введите ваш пол (м/ж) ")

if gender == 'ж':
    gender_ending = 'а'

print(f"Привет {name}, это игра {GAME_NAME}\n")

request = True

while request:
    number = randint(1, MAXIMUM_NUMBER)
    guest = 0
    attempts = 0

    print(f"Я загадал число от 1 до {MAXIMUM_NUMBER}")
    while guest != number:
        guest = input("Какое число я загадал? ")
        while not guest.isdigit() or not (1 <= int(guest) <= MAXIMUM_NUMBER):
            guest = input(f"Просто введи число от 1 до {MAXIMUM_NUMBER} ")

        guest = int(guest)
        if guest > number:
            print(f'Нет, закаданное число меньше чем {guest}\n')
            attempts += 1
        elif guest < number:
            print(f'Нет, закаданное число больше чем {guest}\n')
            attempts += 1
        else:
            print(f'{name}, поздравляю ты угадал{gender_ending}, я загадал число {guest}\n')

    if 11 <= attempts % 100 <= 14:
        end = 'ок'
    elif attempts % 10 == 1:
        end = 'ку'
    elif 1 <= attempts % 100 <= 4:
        end = 'ки'
    else:
        end = 'ок'

    print(f"{name}, ты совершил{gender_ending} {attempts} ошиб{end}")

    total_attempts += attempts
    games += 1

    again = input("Хочешь сыграть еще один раз? (да/нет) ")
    while again != 'нет' and again != 'да':
        again = input("Хочешь сыграть еще один раз? (да/нет) ")
    if again == 'нет':
        request = False


avarge_attempts = total_attempts // games

if 11 <= avarge_attempts % 100 <= 14:
    end_averge = 'ок'
elif avarge_attempts % 10 == 1:
    end_averge = 'ку'
elif 2 <= avarge_attempts % 10 <= 4:
    end_averge = 'ки'
else:
    end_averge = 'ок'

print(f" {name} Спасибо за участие \n")
if avarge_attempts == 0:
    print(f"Поздравляю {name} за все игры ты не совершил{gender_ending} ни одной ошибки! ")
else:
    print(f"в среднем ты совершил{gender_ending} {avarge_attempts} ошиб{end_averge} за игру  ")

if 11 <= games % 100 <= 14:
    end_games = ''
elif games % 10 == 1:
    end_games = 'у'
elif 2 <= games % 10 <= 4:
    end_games = 'ы'
else:
    end_games = ''
print(f"ты сыграл{gender_ending} {games} игр{end_games}")
