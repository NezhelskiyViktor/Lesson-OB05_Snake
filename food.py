import pygame
from random import *



class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(1, 19) * 30
        self.y = randint(1, 19) * 30
        self.food_rect = pygame.Rect(self.x, self.y, 30, 30)
        self.food_img = pygame.image.load('image/food1.png').convert_alpha()
        # Загрузка изображения после инициализации

    def update(self):
        self.x = randint(0, 19) * 30 + 10
        self.y = randint(0, 19) * 30 + 10
        self.food_rect = pygame.Rect(self.x, self.y, 30, 30)

    def draw(self, screen):
        screen.blit(self.food_img, (self.x, self.y))
