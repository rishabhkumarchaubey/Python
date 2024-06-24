import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
PIPE_WIDTH, PIPE_HEIGHT = 80, 600
BIRD_WIDTH, BIRD_HEIGHT = 60, 60
GRAVITY = 0.5
JUMP_HEIGHT = 9
PIPE_GAP = 150
PIPE_SPEED = 4
PIPE_SPAWN_INTERVAL = 180

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Set up the bird
bird_x, bird_y = WIDTH / 3, HEIGHT / 2
bird_vel = 0
bird_rect = pygame.Rect(bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT)

# Set up initial pipes
pipes = []
pipe_timer = 0

# Set up the score
score = 0

# Function to reset the game
def reset_game():
    global bird_y, bird_vel, pipes, pipe_timer, score
    bird_y = HEIGHT / 2
    bird_vel = 0
    pipes = []
    pipe_timer = 0
    score = 0

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = -JUMP_HEIGHT
            elif event.key == pygame.K_r:
                reset_game()

    # Bird movement
    bird_vel += GRAVITY
    bird_y += bird_vel
    bird_rect.y = bird_y

    # Pipe handling
    pipe_timer += 1
    if pipe_timer >= PIPE_SPAWN_INTERVAL:
        pipe_height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        pipes.append(pygame.Rect(WIDTH, 0, PIPE_WIDTH, pipe_height))  # Top pipe
        pipes.append(pygame.Rect(WIDTH, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe_height - PIPE_GAP))  # Bottom pipe
        pipe_timer = 0

    for pipe in pipes:
        pipe.x -= PIPE_SPEED
        if pipe.x + PIPE_WIDTH < 0:
            pipes.remove(pipe)
            continue
        # Collision detection
        if bird_rect.colliderect(pipe):
            reset_game()

        # Score handling
        if pipe.x + PIPE_WIDTH < bird_x and not pipe.x < bird_x:
            score += 0.5  # Increase score by 0.5 for passing each pipe

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, bird_rect)
    for pipe in pipes:
        pygame.draw.rect(screen, WHITE, pipe)
    draw_text(f"Score: {int(score)}", pygame.font.Font(None, 36), WHITE, WIDTH // 2, 50)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
