import tkinter as tk
import random

# Set up main window
window = tk.Tk()
window.title("Ping Pong Game")
canvas = tk.Canvas(window, width=600, height=400, bg="black")
canvas.pack()

# Ball
ball = canvas.create_oval(290, 190, 310, 210, fill="white")
ball_dx, ball_dy = 4, -4

# Paddle
paddle = canvas.create_rectangle(250, 380, 350, 390, fill="white")

# Movement functions
def move_paddle_left(event):
    canvas.move(paddle, -20, 0)

def move_paddle_right(event):
    canvas.move(paddle, 20, 0)

canvas.bind_all("<Left>", move_paddle_left)
canvas.bind_all("<Right>", move_paddle_right)

# Game loop
def game_loop():
    global ball_dx, ball_dy

    # Move ball
    canvas.move(ball, ball_dx, ball_dy)
    pos = canvas.coords(ball)
    paddle_pos = canvas.coords(paddle)

    # Wall collision
    if pos[0] <= 0 or pos[2] >= 600:
        ball_dx = -ball_dx
    if pos[1] <= 0:
        ball_dy = -ball_dy
    if pos[3] >= 400:
        canvas.create_text(300, 200, text="Game Over", fill="red", font=("Arial", 24))
        return

    # Paddle collision
    if (pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]) and (pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]):
        ball_dy = -ball_dy

    window.after(20, game_loop)

game_loop()
window.mainloop()
