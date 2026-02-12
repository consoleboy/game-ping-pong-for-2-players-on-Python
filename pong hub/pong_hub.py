import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Настольный теннис для двух игроков")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10

player1_x, player1_y = 10, HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_x, player2_y = WIDTH - PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT // 2

ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 5 * random.choice([-1, 1]), 5 * random.choice([-1, 1])

paddle_speed = 5
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def reset_ball():
    """Сброс мяча в центр со случайным направлением"""
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_speed_x = 5 * random.choice([-1, 1])
    ball_speed_y = 5 * random.choice([-1, 1])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += paddle_speed

    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Отскок от верхней и нижней стен
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Отскок от левой ракетки
    if (ball_x <= player1_x + PADDLE_WIDTH and 
        ball_x >= player1_x and
        ball_y + BALL_SIZE >= player1_y and 
        ball_y <= player1_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x
        # Добавляем небольшой случайный отскок по вертикали
        ball_speed_y += random.uniform(-1, 1)

    # Отскок от правой ракетки
    if (ball_x + BALL_SIZE >= player2_x and 
        ball_x <= player2_x + PADDLE_WIDTH and
        ball_y + BALL_SIZE >= player2_y and 
        ball_y <= player2_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x
        ball_speed_y += random.uniform(-1, 1)

    # Проверка голов
    if ball_x < 0:
        score2 += 1
        reset_ball()
    if ball_x > WIDTH:
        score1 += 1
        reset_ball()

    # Очистка экрана
    screen.fill(BLACK)

    # Рисуем ракетки
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Рисуем мяч
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Рисуем центральную линию
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Отображаем счет
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 50, 10))

    pygame.display.flip()
    clock.tick(60)
