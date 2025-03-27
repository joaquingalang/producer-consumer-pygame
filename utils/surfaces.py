from sprites.box import *
from utils.settings import *

pygame.font.init()

# Font / Text
label_font = pygame.font.Font(None, 32)

# Title
title_surface = label_font.render('Producer-Consumer Problem', True, (0, 0, 0))
title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))

# Buffer Label
buffer_label_surface = label_font.render('Buffer Queue: ', True, (0, 0, 0))
buffer_label_rect = buffer_label_surface.get_rect()
buffer_label_rect.topleft = (100, 275)

# Status Label
status_label_surface = label_font.render('Status: ', True, (0, 0, 0))
status_label_rect = status_label_surface.get_rect()
status_label_rect.topleft = (100, 400)

# Producer Label Button
prod_label_button = LabelBox('Producers', '#F59393', LABEL_RECT_SIZE, ((SCREEN_WIDTH // 2) - 100 - LABEL_RECT_SIZE[0], 75))

# Consumer Label Button
con_label_button = LabelBox('Consumers', '#F59393', LABEL_RECT_SIZE, ((SCREEN_WIDTH // 2) + 100, 75))

# Add Producer Button
prod_add_button = LabelBox('+', '#5C8E19', MIN_BOX_SIZE, ((SCREEN_WIDTH // 2) - 300 - MIN_BOX_SIZE[0], 75), font_size=32, text_color="#FFFFFF")

# Add Consumer Button
con_add_button = LabelBox('+', '#5C8E19', MIN_BOX_SIZE, ((SCREEN_WIDTH // 2) + 50, 75), font_size=32, text_color="#FFFFFF")

# Subtract Producer Button
prod_sub_button = LabelBox('-', '#BC371C', MIN_BOX_SIZE, ((SCREEN_WIDTH // 2) - 50 - MIN_BOX_SIZE[0], 75), font_size=32, text_color="#FFFFFF")

# Subtract Consumer Button
con_sub_button = LabelBox('-', '#BC371C', MIN_BOX_SIZE, ((SCREEN_WIDTH // 2) + 300, 75), font_size=32, text_color="#FFFFFF")

# Locked Label
locked_surface = LabelBox('LOCKED', '#D3D3D3', COUNTER_RECT_SIZE, (SCREEN_WIDTH // 2 - 350, 205))

# Draw Producer & Consumer Counters
def draw_counters(screen, prod_count, con_count):
    producer_counter = CounterBox('Producers:', prod_count, '#F5C5C5', COUNTER_RECT_SIZE, ((SCREEN_WIDTH // 2) - 350, 425))
    screen.blit(producer_counter.image, producer_counter.rect)

    consumer_counter = CounterBox('Consumers:', con_count, '#F5C5C5', COUNTER_RECT_SIZE, ((SCREEN_WIDTH // 2) + 50, 425))
    screen.blit(consumer_counter.image, consumer_counter.rect)

    # Producer & Consumer Controller Divider
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH // 2, 430), (SCREEN_WIDTH // 2, 470), 4)

def display_elements(screen, producers, consumers, buffer):

    # Title Label
    screen.blit(title_surface, title_rect)

    # Producer Controller
    prod_label_button.draw(screen)
    prod_add_button.draw(screen)
    prod_sub_button.draw(screen)

    # Producer & Consumer Controller Divider
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH // 2, 80), (SCREEN_WIDTH // 2, 120), 4)

    # Consumer Controller
    con_label_button.draw(screen)
    con_add_button.draw(screen)
    con_sub_button.draw(screen)

    # Producer Boxes
    for index, prod in enumerate(producers):
        box_content = str(prod.value) if prod.value is not None else ''
        box = BoxSmall(box_content)
        box.rect.topleft = (index * 62 + 100, 140)
        box.draw(screen)

    # Locked Box
    screen.blit(locked_surface.image, locked_surface.rect)

    # Consumer Boxes
    for index, con in enumerate(consumers):
        box_content = str(con.store) if con.store is not None else ''
        box = BoxSmall(box_content)
        box.rect.topleft = (index * 62 + 500, 140)
        box.draw(screen)

    # Buffer Label
    screen.blit(buffer_label_surface, buffer_label_rect)

    # Draw Buffer Boxes
    last_index = 0
    for index, value in enumerate(buffer):
        last_index = index
        box_content = str(value) if value is not None else ''
        box = BoxLarge(box_content, '#F59393')
        box.rect.topleft = (index * 89 + 100, 300)
        box.draw(screen)

    # Fill the rest of the buffer with empty boxes
    start_index = last_index if (len(buffer) == 0) else last_index + 1
    for index in range(start_index, 8):
        box = BoxLarge('')
        box.rect.topleft = (index * 89 + 100, 300)
        box.draw(screen)

    # Status Label
    screen.blit(status_label_surface, status_label_rect)

    # Counters
    draw_counters(screen, len(producers), len(consumers))