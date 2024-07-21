import pygame
import random

# Задаем размеры экрана и скорость игры
WIDTH, HEIGHT = 480, 480
FPS = 10
CELL_SIZE = 20

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Snake:
    def __init__(self):
        self.positions = [(WIDTH//2, HEIGHT//2)]
        self.direction = (0, -CELL_SIZE)
        self.grow = False

    def change_direction(self, dir):
        if (dir[0] * -1, dir[1] * -1) != self.direction:
            self.direction = dir

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = ((cur[0] + x) % WIDTH, (cur[1] + y) % HEIGHT)
        if new in self.positions[2:]:
            self.positions = [(WIDTH//2, HEIGHT//2)]
            self.direction = (0, -CELL_SIZE)
        else:
            self.positions.insert(0, new)
            if not self.grow:
                self.positions.pop()
            self.grow = False

    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, GREEN, (pos[0], pos[1], CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH//CELL_SIZE)-1) * CELL_SIZE,
                         random.randint(0, (HEIGHT//CELL_SIZE)-1) * CELL_SIZE)

    def respawn(self):
        self.position = (random.randint(0, (WIDTH//CELL_SIZE)-1) * CELL_SIZE,
                         random.randint(0, (HEIGHT//CELL_SIZE)-1) * CELL_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Загрузка изображения фона
background_image= pygame.image.load('snakes.jpg')

# Инициализация объектов змейки и еды
snake = Snake()
food = Food()
sound = pygame.mixer.Sound("drakon.wav")
sound.play()
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL_SIZE, 0))

    # Обновление состояния игры
    snake.move()
    if snake.positions[0] == food.position:
        snake.grow_snake()
        food.respawn()

    # Рендеринг
    screen.blit(background_image, (0, 0))  # Отрисовка фона
    snake.draw(screen)
    food.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()