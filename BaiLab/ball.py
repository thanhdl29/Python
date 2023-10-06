import pygame
import sys
import random


pygame.init()


width, height = 600, 400
paddle_width, paddle_height = 100, 10
ball_size = 20
brick_width, brick_height = 60, 20
brick_rows = 5
brick_cols = 10
paddle_speed = 10
ball_speed = 5


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")


paddle_x = (width - paddle_width) // 2
paddle_y = height - 2 * paddle_height
ball_x = random.randint(0, width - ball_size)
ball_y = height - 2 * paddle_height - ball_size
ball_dx = random.choice([-1, 1])  
ball_dy = -1 
bricks = []


for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * (brick_width + 5), row * (brick_height + 5), brick_width, brick_height)
        bricks.append(brick)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

   
    ball_x += ball_dx * ball_speed
    ball_y += ball_dy * ball_speed

   
    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and paddle_y < ball_y < paddle_y + paddle_height
    ):
        ball_dy = -1

   
    for brick in bricks:
        if brick.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
            ball_dy = 1
            bricks.remove(brick)


    if ball_x <= 0 or ball_x + ball_size >= width:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy = 1

  
    if ball_y + ball_size >= height:
        ball_x = random.randint(0, width - ball_size)
        ball_y = height - 2 * paddle_height - ball_size
        ball_dy = -1

   
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, red, (ball_x, ball_y, ball_size, ball_size))

  
    for brick in bricks:
        pygame.draw.rect(screen, blue, brick)

 
    pygame.display.flip()

  
    pygame.time.Clock().tick(30)