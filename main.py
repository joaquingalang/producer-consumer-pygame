import pygame
import sys
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
COOLDOWN = 200  # Cooldown duration in milliseconds
last_click_time = 0  # Tracks the last time a click was processed

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

    # Input Checks
    mouse_pos = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
    if pygame.mouse.get_pressed()[0] and current_time - last_click_time > COOLDOWN:
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

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()