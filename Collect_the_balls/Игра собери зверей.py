from random import randint
import pygame as pg
from ball10 import Ball
# Инициализируем pygame
pg.init()
game = True
W,H = 600,400
# задаем USEREVENT каждые 2000 миллисекунд для создания (новых падающих кружков)
pg.time.set_timer(pg.USEREVENT, 1500)

# создаем экран
sc = pg.display.set_mode((W, H))
# Задаем картинку и название окна игры
pg.display.set_caption("Собери зверей")
pg.display.set_icon(pg.image.load("Collect_the_balls/images/img1.jpg"))

# создаем переменные для отслеживания FPS 
clock = pg.time.Clock()
FPS = 60

# ЦВЕТА для использования во время игры
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

# фон для отображения собранных очков в игре
bg_point = pg.image.load('Collect_the_balls/images/score_fon.png')
f = pg.font.SysFont('arial', 30)

# скорость движения и парамметры ТЕЛЕГА 
speed = 10
telega = pg.image.load('Collect_the_balls/images/telega.png')
t_rect = telega.get_rect(centerx=W//2, bottom=H-5)

# Задаем ФОНОВАЯ КАРТИНКА для нашей игры
bg_surf = pg.image.load("Collect_the_balls/images/back1.jpg").convert()
bg_surf = pg.transform.scale(bg_surf, (bg_surf.get_width()-100, bg_surf.get_height()-180))

# Создаем список и группу с используемыми КРУГИ и в последствии в функции рандомно им 
# задаем парраметры скорости и положение по оси X
balls_data = [{'path':'ball_bear.png', 'score': 200},
              {'path':'ball_fox.png', 'score': 150}, 
              {'path':'ball_panda.png', 'score': 250},
              {'path':'bomb.png', 'score': False}
              ]
balls_surf = [pg.image.load("Collect_the_balls/images/"+data['path']).convert_alpha() for data in balls_data]

balls_group = pg.sprite.Group()

def creat_balls(group):
    indx = randint(0,len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1,4)
    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'],  group)
   
# очки набранные во время игры и пороги новых левлов
game_score = 0 
next_level = 500
level = 1
# функция отслеживающая поподания кругов в телегу

def collide_balls():
    global game_score
    for ball in balls_group:
        if t_rect.collidepoint(ball.rect.center):
            if ball.score == False:
                return False
            else:
                game_score += ball.score
            ball.kill()
    return True

 
creat_balls(balls_group
            )

# Основной цикл для работы во время программы
while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.USEREVENT:
            creat_balls(balls_group)
    keys = pg.key.get_pressed()
    
    # проверка на нажатие левой или правой стрелки и котнроль за границей окна
    if keys[pg.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x <= 0:
            t_rect.x = 0
    elif keys[pg.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > W - t_rect.width :
            t_rect.x = W - t_rect.width
    elif keys[pg.K_SPACE]:
        new_game = True
        
                

    # функция отслеживающая поподания кругов в телегу
    if collide_balls():
        sc.blit(bg_surf, (0, 0))
        # отображение очков
        sc.blit(bg_point,(0,0))
        sc_text = f.render(str(game_score), 1, WHITE)   
        sc.blit(sc_text, (20,10))
        # отображение кругов, телеги
        balls_group.draw(sc)
        sc.blit(telega, t_rect)
        pg.display.update()
        
        clock.tick(FPS)
        balls_group.update(H)
    else:
        
        sc.blit(bg_surf, (0, 0))
        sc.blit(bg_point,(W//2,H//2))
        sc.blit(sc_text, (W//2+60,H//2+20))
        pg.display.update()
        clock.tick(FPS)
        

        
        
        
        