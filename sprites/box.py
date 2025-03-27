import pygame

class BoxSmall(pygame.sprite.Sprite):
    def __init__(self, label, color='#F5C5C5', position=(0,0), font_size=24, text_color="#000000"):
        super().__init__()
        pygame.font.init()
        self.label = label
        self.image = pygame.Surface((50, 50))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # Font setup
        self.font = pygame.font.Font(None, font_size)  # Use default font
        self.text_color = pygame.Color(text_color)

        # Render the label text
        self.text_surface = self.font.render(self.label, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.image.get_rect().center)

        # Blit the text onto the button surface
        self.image.blit(self.text_surface, self.text_rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class BoxLarge(pygame.sprite.Sprite):
    def __init__(self, label, color='#F5C5C5', position=(0,0), font_size=24, text_color="#000000"):
        super().__init__()
        pygame.font.init()
        self.label = label
        self.image = pygame.Surface((75, 75))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # Font setup
        self.font = pygame.font.Font(None, font_size)  # Use default font
        self.text_color = pygame.Color(text_color)

        # Render the label text
        self.text_surface = self.font.render(self.label, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.image.get_rect().center)

        # Blit the text onto the button surface
        self.image.blit(self.text_surface, self.text_rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class LabelBox(pygame.sprite.Sprite):
    def __init__(self, label, color, size, position, font_size=24, text_color="#000000"):
        super().__init__()
        pygame.font.init()
        self.label = label
        self.image = pygame.Surface(size)
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # Font setup
        self.font = pygame.font.Font(None, font_size)  # Use default font
        self.text_color = pygame.Color(text_color)

        # Render the label text
        self.text_surface = self.font.render(self.label, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.image.get_rect().center)

        # Blit the text onto the button surface
        self.image.blit(self.text_surface, self.text_rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class CounterBox(pygame.sprite.Sprite):
    def __init__(self, label, count, color, size, position, font_size=24, text_color="#000000"):
        super().__init__()
        pygame.font.init()
        self.label = label
        self.count = count
        self.image = pygame.Surface(size)
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        # Font setup
        self.font = pygame.font.Font(None, font_size)  # Use default font
        self.text_color = pygame.Color(text_color)

        # Render the label text
        self.text_surface = self.font.render(self.label, True, self.text_color)
        text_image_rect = self.image.get_rect().topleft
        self.text_rect = self.text_surface.get_rect(topleft=(text_image_rect[0]+18, text_image_rect[1]+18))

        # Blit the text onto the button surface
        self.image.blit(self.text_surface, self.text_rect)

        # Render counter text
        self.counter_surface = self.font.render(str(self.count), True, self.text_color)
        counter_image_rect = self.image.get_rect().topright
        self.counter_rect = self.counter_surface.get_rect(topright=(counter_image_rect[0]-30, counter_image_rect[1]+18))

        # Blit the counter onto the button surface
        self.image.blit(self.counter_surface, self.counter_rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)