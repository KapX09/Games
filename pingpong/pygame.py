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


pygame.quit()
sys.exit()
