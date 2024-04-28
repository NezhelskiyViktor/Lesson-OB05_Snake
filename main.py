import pygame
import sys
from random import *
import time


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self._r = 30
        self.body_list = [['D', pygame.Rect(self.x, self.y, 30, 30)], \
                          ['D', pygame.Rect(self.x, self.y - self._r, 30, 30)], \
                          ['D', pygame.Rect(self.x, self.y - self._r * 2, 30, 30)], \
                          ['D', pygame.Rect(self.x, self.y - self._r * 3, 30, 30)]]

    def move(self):
        if direction == 'L':
            self.x -= shift
        elif direction == 'R':
            self.x += shift
        elif direction == 'U':
            self.y -= shift
        elif direction == 'D':
            self.y += shift
        self.body_list.insert(0, [direction, pygame.Rect(self.x, self.y, 30, 30)])
        self.body_list[1][0] = direction
        self.body_list.pop(-1)
        self.draw()

    def draw(self):
        # Отрисовка середины змейки
        for i in self.body_list[1:-1]:
            if i[0] == 'L':
                screen.blit(snake_skill_L, (i[1].x, i[1].y))
            elif i[0] == 'R':
                screen.blit(snake_skill_R, (i[1].x, i[1].y))
            elif i[0] == 'U':
                screen.blit(snake_skill_U, (i[1].x, i[1].y))
            elif i[0] == 'D':
                screen.blit(snake_skill_U, (i[1].x, i[1].y))
        # Отрисовка хвоста змейки
        if self.body_list[-1][0] == 'L':
            screen.blit(snake_tail_L, (self.body_list[-1][1].x, self.body_list[-1][1].y))
        elif self.body_list[-1][0] == 'R':
            screen.blit(snake_tail_R, (self.body_list[-1][1].x, self.body_list[-1][1].y))
        elif self.body_list[-1][0] == 'U':
            screen.blit(snake_tail_U, (self.body_list[-1][1].x, self.body_list[-1][1].y))
        elif self.body_list[-1][0] == 'D':
            screen.blit(snake_tail_D, (self.body_list[-1][1].x, self.body_list[-1][1].y))
        # Отрисовка головы змейки
        if self.body_list[0][0] == 'L':
            screen.blit(snake_img_L, (self.body_list[0][1].x, self.body_list[0][1].y))
        elif self.body_list[0][0] == 'R':
            screen.blit(snake_img_R, (self.body_list[0][1].x, self.body_list[0][1].y))
        elif self.body_list[0][0] == 'U':
            screen.blit(snake_img_U, (self.body_list[0][1].x, self.body_list[0][1].y))
        elif self.body_list[0][0] == 'D':
            screen.blit(snake_img_D, (self.body_list[0][1].x, self.body_list[0][1].y))


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(0, 19) * 30
        self.y = randint(0, 19) * 30
        self.food_rect = pygame.Rect(self.x, self.y, 30, 30)

    def update(self):
        self.x = randint(0, 19) * 30
        self.y = randint(0, 19) * 30
        self.food_rect = pygame.Rect(self.x, self.y, 30, 30)

    def draw(self):
        screen.blit(food_img, (self.x, self.y))


pygame.init()
pygame.mouse.set_visible(False)
FPS = 60
clock = pygame.time.Clock()
screen_width, screen_height = 600, 600
# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
# Прямоугольник, представляющий границы экрана
boundary_rect = pygame.Rect(30, 30, screen_width - 30, screen_height - 30)
bg = pygame.image.load('image/field.jpg').convert()
food_img = pygame.image.load('image/food1.png').convert_alpha()
snake_img_L = pygame.image.load('image/snake_L.png').convert_alpha()
snake_img_R = pygame.image.load('image/snake_R.png').convert_alpha()
snake_img_U = pygame.image.load('image/snake_U.png').convert_alpha()
snake_img_D = pygame.image.load('image/snake_D.png').convert_alpha()
snake_skill_L = pygame.image.load('image/snake_skill_L.jpg').convert()
snake_skill_R = pygame.image.load('image/snake_skill_R.jpg').convert()
snake_skill_U = pygame.image.load('image/snake_skill_U.jpg').convert()
snake_skill_D = pygame.image.load('image/snake_skill_D.jpg').convert()
snake_tail_L = pygame.image.load('image/snake_tail_L.png').convert_alpha()
snake_tail_R = pygame.image.load('image/snake_tail_R.png').convert_alpha()
snake_tail_U = pygame.image.load('image/snake_tail_U.png').convert_alpha()
snake_tail_D = pygame.image.load('image/snake_tail_D.png').convert_alpha()

pygame.display.set_caption('Змейка')

# Скорость движения
shift = 30
snake = Snake(screen_width // 2, screen_height // 2)
direction = 'D'
food = Food()
takt = 0
game_continues = True

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = 'L'
    elif keys[pygame.K_RIGHT]:
        direction = 'R'
    elif keys[pygame.K_UP]:
        direction = 'U'
    elif keys[pygame.K_DOWN]:
        direction = 'D'

    # Проверяем столкновение с границей экрана

    if not takt % 15:
        game_continues = snake.body_list[0][1].colliderect(boundary_rect)

        # Проверка столкновения
        collision = snake.body_list[0][1].colliderect(food.food_rect)
        if collision:
            food.update()
            snake.body_list.append(snake.body_list[-1])
        if game_continues:
            # Очистка экрана
            screen.blit(bg, (0, 0))
            # Рисование snake и food
            food.draw()
            snake.move()
        else:
            screen.fill((0, 0, 0))
            pygame.display.set_caption('Игра окончена')



    # Обновление экрана
    pygame.display.flip()

    # Задержка для снижения скорости цикла
    clock.tick(FPS)
    takt -= game_continues
pygame.quit()
sys.exit()
