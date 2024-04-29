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

    def update(self, snake):
        repeat = True
        while repeat:
            self.x = randint(1, 19) * 30
            self.y = randint(1, 19) * 30
            self.food_rect = pygame.Rect(self.x, self.y, 30, 30)
            for i in snake.body_list:
                if self.food_rect.colliderect(i[1]):
                    repeat = True
                    break
                else:
                    repeat = False

    def draw(self, screen):
        screen.blit(self.food_img, (self.x, self.y))
