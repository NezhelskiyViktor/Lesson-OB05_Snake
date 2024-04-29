import pygame
import sys
from food import Food
from snake import Snake


def game_proceccing(direction, snake, food, boundary_rect, screen, bg, takt):
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
    game_continues = snake.body_list[0][1].colliderect(boundary_rect)

    if not takt % 15:
        # Проверка столкновения
        collision = snake.body_list[0][1].colliderect(food.food_rect)
        if collision:
            food.update(snake)
            snake.body_list.append(snake.body_list[-1])
        if game_continues:
            # Очистка экрана
            screen.fill((130, 180, 50))
        else:
            screen.fill((0, 0, 0))
            pygame.display.set_caption(
                f'Змейка съела {len(snake.body_list) - 4} лягушек. \
                Нажмите <пробел> для продолжения')
        screen.blit(bg, (30, 30))
        # Рисование snake и food
        food.draw(screen)
        if game_continues:
            snake.move(screen, direction, shift)
        else:
            snake.draw(screen)
    return direction

pygame.init()
pygame.mouse.set_visible(False)
FPS = 60
clock = pygame.time.Clock()
# Создание экрана
screen_width, screen_height = 660, 660
screen = pygame.display.set_mode((screen_width, screen_height))
# Прямоугольник, представляющий границы экрана
boundary_rect = pygame.Rect(40, 40, screen_width - 80, screen_height - 80)
bg = pygame.image.load('image/field.jpg').convert()

pygame.display.set_caption('Змейка')

# Скорость движения
shift = 30
snake = Snake(screen_width // 2, screen_height // 2)
food = Food()
food.update(snake)
game_continues = True
direction = 'D'
takt = 0

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_continues = True
                pygame.display.set_caption('Змейка')
                direction = 'D'
                snake = Snake(screen_width // 2, screen_height // 2)
                food = Food()
                food.update(snake)
    direction = game_proceccing(direction, snake, food, boundary_rect, screen, bg, takt)
    # Обновление экрана
    pygame.display.flip()

    # Задержка для снижения скорости цикла
    clock.tick(FPS)
    takt -= 1
pygame.quit()
sys.exit()
