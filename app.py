import pygame
import time
import random

# Initialize the game
pygame.init()

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the width and height of the display window
width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set the speed of the snake
snake_speed = 15

# Define the font style and size
font_style = pygame.font.SysFont(None, 50)

# Define the score font style and size
score_font = pygame.font.SysFont(None, 35)

# Function to display the score
def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    display.blit(value, [0, 0])

# Function to display the snake on the screen
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Function to run the game
def run_game():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # Change in position of the snake
    x1_change = 0
    y1_change = 0

    # Define the length of the snake and the size of each block
    snake_list = []
    length_of_snake = 1
    snake_block = 10

    # Generate random positions for the food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            # Display game over message and options to play again or quit
            display.fill(black)
            game_over_message = font_style.render("Game Over!", True, red)
            play_again_message = font_style.render("Press P-Play Again or Q-Quit", True, red)
            display.blit(game_over_message, [width / 3, height / 3])
            display.blit(play_again_message, [width / 3.5, height / 2.5])
            show_score(length_of_snake - 1)
            pygame.display.update()

            # Check for user input to play again or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        run_game()  # Restart the game
                    elif event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the boundaries of the display window
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        display.fill(black)
        pygame.draw.rect(display, blue, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()
