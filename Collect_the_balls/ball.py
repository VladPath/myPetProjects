from typing import Any
import pygame as pg


class Ball(pg.sprite.Sprite):
    def __init__(self, x:int, speed:int, surf:str, group:str) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x,-20))
        self.speed = speed
        self.add(group)
    
    def update(self, *args: Any) -> None:
        if self.rect.y <= args[0] + 10:
            self.rect.y += self.speed 
        else:
            self.kill()
            
        
        