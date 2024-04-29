import pygame


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

        self.snake_img_L = pygame.image.load('image/snake_L.png').convert_alpha()
        self.snake_img_R = pygame.transform.rotate(self.snake_img_L, 180)
        self.snake_img_U = pygame.transform.rotate(self.snake_img_L, 270)
        self.snake_img_D = pygame.transform.rotate(self.snake_img_L, 90)
        self.snake_skill_L = pygame.image.load('image/snake_skill_L.jpg').convert()
        self.snake_skill_R = pygame.transform.rotate(self.snake_skill_L, 180)
        self.snake_skill_U = pygame.transform.rotate(self.snake_skill_L, 270)
        self.snake_skill_D = pygame.transform.rotate(self.snake_skill_L, 90)
        self.snake_tail_L = pygame.image.load('image/snake_tail_L.png').convert_alpha()
        self.snake_tail_R = pygame.transform.rotate(self.snake_tail_L, 180)
        self.snake_tail_U = pygame.transform.rotate(self.snake_tail_L, 270)
        self.snake_tail_D = pygame.transform.rotate(self.snake_tail_L, 90)

    def move(self, screen, direction, shift):
        if direction == 'L':
            self.x -= shift
        elif direction == 'R':
            self.x += shift
        elif direction == 'U':
            self.y -= shift
        elif direction == 'D':
            self.y += shift

        self.update(direction)
        self.draw(screen)

    def draw(self, screen):
        # Отрисовка середины змейки
        for i in self.body_list[1:-1]:
            if i[0] == 'L':
                screen.blit(self.snake_skill_L, (i[1].x, i[1].y))
            elif i[0] == 'R':
                screen.blit(self.snake_skill_R, (i[1].x, i[1].y))
            elif i[0] == 'U':
                screen.blit(self.snake_skill_U, (i[1].x, i[1].y))
            elif i[0] == 'D':
                screen.blit(self.snake_skill_U, (i[1].x, i[1].y))
        # Отрисовка хвоста змейки
        if self.body_list[-1][0] == 'L':
            screen.blit(self.snake_tail_L, (self.body_list[-1][1].x, self.body_list[-1][1].y))
        elif self.body_list[-1][0] == 'R':
            screen.blit(self.snake_tail_R, (self.body_list[-1][1].x, self.body_list[-1][1].y))
        elif self.body_list[-1][0] == 'U':
            screen.blit(self.snake_tail_U, (self.body_list[-1][1].x, self.body_list[-1][1].y))
        elif self.body_list[-1][0] == 'D':
            screen.blit(self.snake_tail_D, (self.body_list[-1][1].x, self.body_list[-1][1].y))
        # Отрисовка головы змейки
        if self.body_list[0][0] == 'L':
            screen.blit(self.snake_img_L, (self.body_list[0][1].x, self.body_list[0][1].y))
        elif self.body_list[0][0] == 'R':
            screen.blit(self.snake_img_R, (self.body_list[0][1].x, self.body_list[0][1].y))
        elif self.body_list[0][0] == 'U':
            screen.blit(self.snake_img_U, (self.body_list[0][1].x, self.body_list[0][1].y))
        elif self.body_list[0][0] == 'D':
            screen.blit(self.snake_img_D, (self.body_list[0][1].x, self.body_list[0][1].y))

    def update(self, direction):
        self.body_list.insert(0, [direction, pygame.Rect(self.x, self.y, 30, 30)])
        self.body_list[1][0] = direction
        self.body_list.pop(-1)


