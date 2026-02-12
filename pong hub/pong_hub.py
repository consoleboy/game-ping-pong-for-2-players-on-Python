import pygame
import sys


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
ball_speed_x, ball_speed_y = 5, 5


paddle_speed = 5

clock = pygame.time.Clock()

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

    
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

   
    if (ball_x <= player1_x + PADDLE_WIDTH and
        player1_y < ball_y < player1_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x

    
    if (ball_x >= player2_x - BALL_SIZE and
        player2_y < ball_y < player2_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x

   
    if ball_x < 0 or ball_x > WIDTH:
       
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = -ball_speed_x

   
    screen.fill(BLACK)

    
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    
    pygame.display.flip()
    clock.tick(60)