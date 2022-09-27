import sys

import random

import pygame
from pygame.time import Clock

# create first game window

# initialize pygame
pygame.init()
pygame.font.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and icon
pygame.display.set_caption("Super duper game")
icon = pygame.image.load('cauldron.png')
pygame.display.set_icon(icon)

# Player

player_img = pygame.image.load('space.png')
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

# Enemy

enemy_img = pygame.image.load('alien(1).png')
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x = change = 0


# Score

score = 0


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Game Loop
running = True

while running:

    pygame.time.Clock().tick_busy_loop(144)

    screen.fill((0, 0, 0))
    game_time_ms = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_UP:
                player_y_change = -1
            if event.key == pygame.K_DOWN:
                player_y_change = 1


    # RGB - red, green, blue
    screen.fill((0, 150, 150))

    player_x += player_x_change
    player_y += player_y_change

    if player_x <= 0:
        player_x = 0
        player_x_change = player_x_change * -1

    elif player_x >= 768:
        player_x = 768
        player_x_change = player_x_change * -1

    if player_y <= 0:
        player_y = 0
        player_y_change = player_y_change * -1

    elif player_y > 568:
        player_y = 568
        player_y_change = player_y_change * -1

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    offset = 50
    if player_x <= enemy_x + offset & player_x >= enemy_x - offset:
        if player_y <= enemy_y + offset & player_y >= enemy_y - offset:
            print("Score += 1")
            score += 1
            print("Score: " + str(score))

    pygame.display.update()
