import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Single Player Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (30, 30, 30)

# Paddle setup
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 8

# Ball setup
BALL_SIZE = 20
MAX_SPEED = 12
SPEED_INCREASE_FACTOR = 1.03

# Font
font = pygame.font.SysFont("Courier", 32)

clock = pygame.time.Clock()

def draw_instructions_screen():
    WIN.fill(BLACK)
    small_font = pygame.font.SysFont("Courier", 20)

    # Full box lines that cover instructions inside
    box_lines = [
        "+*****************************",
        "+                            +",
        "+    Single-Player Pong      +",
        "+    -------------------     +",
        "+                            +",
        "+                            +",
        "+    Controls:               +",
        "+     Up / Down arrows       +",
        "+     P - Pause / Unpause    +",
        "+     R - Restart            +",
        "+                            +",
        "+    Press ENTER to start    +",
        "+                            +",
        "+                            +",
        "******************************"   
        ]
    
    line_height = small_font.get_height()
    total_height = line_height * len(box_lines)
    start_y = (HEIGHT - total_height) // 2  # vertical center

    for i, line in enumerate(box_lines):
        text_surface = small_font.render(line, True, WHITE)
        line_width = text_surface.get_width()
        start_x = (WIDTH - line_width) // 2  # horizontal center per line
        WIN.blit(text_surface, (start_x, start_y + i * line_height))

    pygame.display.flip()


def reset_game():
    global paddle, ball, ball_dx, ball_dy, score, hit_count, game_over, paused
    paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
    ball_dx = 5
    ball_dy = 5
    score = 0
    hit_count = 0
    game_over = False
    paused = False

# Initialize game variables
paused = False
game_over = False
score = 0
hit_count = 0
ball_dx = 5
ball_dy = 5

# Create paddle and ball Rects
paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Start screen flag
start_screen = True

# Main loop
running = True
while running:
    clock.tick(60)

    if start_screen:
        draw_instructions_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_screen = False
                    reset_game()
        continue

    # Game screen logic
    WIN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Pause/unpause
            if event.key == pygame.K_p and not game_over:
                paused = not paused
            # Restart game
            if event.key == pygame.K_r and game_over:
                reset_game()

    keys = pygame.key.get_pressed()
    if not paused and not game_over:
        # Paddle movement
        if keys[pygame.K_UP] and paddle.top > 0:
            paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle.bottom < HEIGHT:
            paddle.y += PADDLE_SPEED

        # Ball movement
        ball.x += ball_dx
        ball.y += ball_dy

        # Bounce off top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy *= -1

        # Bounce off right wall
        if ball.right >= WIDTH:
            ball.right = WIDTH
            ball_dx *= -1
            score += 1

        # Paddle collision
        if ball.colliderect(paddle):
            ball.left = paddle.right
            ball_dx *= -1
            hit_count += 1

            if hit_count % 5 == 0 and abs(ball_dx) < MAX_SPEED:
                ball_dx *= SPEED_INCREASE_FACTOR
                ball_dy *= SPEED_INCREASE_FACTOR

        # Game over if missed
        if ball.left <= 0:
            game_over = True

    # Draw paddle and ball
    pygame.draw.rect(WIN, WHITE, paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # Pause message
    if paused:
        pause_text = font.render("PAUSED", True, WHITE)
        WIN.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - 20))

    # Game over message
    if game_over:
        game_over_text = font.render("Game Over! Press R to Restart", True, WHITE)
        WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()

