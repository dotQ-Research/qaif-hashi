import pygame
import sys

# Constants for colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = "Arial"
FONT_SIZE = 36

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hashi Game Menu")

# Create a font for the menu text
font = pygame.font.SysFont(FONT, FONT_SIZE)

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Menu loop
while True:
    screen.fill(WHITE)

    # Draw menu options
    draw_text("Hashi Game Menu", screen_width // 2, 100)
    draw_text("1. Start Game", screen_width // 2, 200)
    draw_text("2. Instructions", screen_width // 2, 250)
    draw_text("3. Quit", screen_width // 2, 300)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                # Start the game here (replace with your game code)
                print("Starting the game...")
            elif event.key == pygame.K_2:
                # Show instructions here
                print("Displaying instructions...")
            elif event.key == pygame.K_3:
                pygame.quit()
                sys.exit()
