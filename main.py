import pygame
import sys
from random import randint
from utils.settings import *
from utils.surfaces import *
from models.prod_con_environment import ProdConEnvironment
from models.producer import Producer
from models.consumer import Consumer

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Producer-Consumer Problem')

# Setup simulation environment
simulation = ProdConEnvironment()

# Buttons
buttons = {
    "prod_add": prod_add_button,
    "con_add": con_add_button,
    "prod_sub": prod_sub_button,
    "con_sub": con_sub_button
}

# Cooldown settings
CLICK_COOLDOWN = 200  # Cooldown duration in milliseconds
last_click_time = 0  # Tracks the last time a click was processed

UPDATE_COOLDOWN = 1500  # Cooldown duration in milliseconds
last_update_time = 0  # Tracks the last time the simulation was updated

simulation.buffer = [24, 3, 11]

# Main "Game" Loop
running = True
while running:
    
    # Event Loop (Fetches events such as user input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill The Screen w/ White
    screen.fill((245, 245, 245))

    # Display Surfaces
    display_elements(screen, simulation.producers, simulation.consumers, simulation.buffer)
    screen.blit(locked_surface.image, locked_surface.rect)

    # Input Checks
    mouse_pos = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
    if pygame.mouse.get_pressed()[0] and current_time - last_click_time > CLICK_COOLDOWN:
        last_click_time = current_time  # Update the last click time
        for key, button in buttons.items():
            if button.rect.collidepoint(mouse_pos):
                if key == "prod_add":
                    simulation.add_prod()
                elif key == "con_add":
                    simulation.add_con()
                elif key == "prod_sub":
                    simulation.delete_prod()
                elif key == "con_sub":
                    simulation.delete_con()
        print(f"Mouse Clicked at: {mouse_pos}")
        print(f"Buffer Size: {len(simulation.buffer)}")
        print(f"Producers: {len(simulation.producers)}")
        print(f"Consumers: {len(simulation.consumers)}")

    # Update Simulation Every 1.5 Seconds
    if (current_time - last_update_time) > UPDATE_COOLDOWN:
        last_update_time = current_time
        total_prod_and_con = len(simulation.producers) + len(simulation.consumers)

        if (total_prod_and_con > 0):

            # Consume
            simulation.consume()

            # Determine Turn Taker
            if (len(simulation.buffer) == 0 and len(simulation.producers) != 0):
                locked_surface.rect.topleft = (SCREEN_WIDTH // 2 - 350, 205)
                simulation.insert_data()
            elif (len(simulation.buffer) == 8 and len(simulation.consumers) != 0):
                locked_surface.rect.topleft = (SCREEN_WIDTH // 2 + 50, 205)
                simulation.remove_data()
            else:
                prod_chance = len(simulation.producers) / total_prod_and_con
                turn_taker = randint(1, 100 + 1)
                print(turn_taker, prod_chance * 100)
                if (turn_taker <= int(prod_chance * 100)):
                    locked_surface.rect.topleft = (SCREEN_WIDTH // 2 - 350, 205)
                    simulation.insert_data()
                else:
                    locked_surface.rect.topleft = (SCREEN_WIDTH // 2 + 50, 205)
                    simulation.remove_data()

            # Produce
            simulation.produce()


    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()