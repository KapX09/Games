import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Single Player Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
PADDLE_SPEED = 8

# Ball
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_dx = 5
ball_dy = 5

# Score
score = 0
font = pygame.font.SysFont("Courier", 32)

# Speed control
hit_count = 0
SPEED_INCREASE_FACTOR = 1.03
MAX_SPEED = 12

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    WIN.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle.bottom < HEIGHT:
        paddle.y += PADDLE_SPEED

    # Move ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Bounce off top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Bounce off right wall (score)
    if ball.right >= WIDTH:
        ball_dx *= -1
        score += 1

    # Collision with paddle
    if ball.colliderect(paddle):
        ball.left = paddle.right
        ball_dx *= -1
        hit_count += 1

        if hit_count % 5 == 0 and abs(ball_dx) < MAX_SPEED:
            ball_dx *= SPEED_INCREASE_FACTOR
            ball_dy *= SPEED_INCREASE_FACTOR

    # Missed the ball (game over)
    if ball.left <= 0:
        running = False

    # Draw everything
    pygame.draw.rect(WIN, WHITE, paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.line(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)

    score_text = font.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()

# Game over screen
WIN.fill(BLACK)
game_over_text = font.render("Game Over!", True, WHITE)
score_text = font.render(f"Final Score: {score}", True, WHITE)
WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 40))
WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 10))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
sys.exit()
