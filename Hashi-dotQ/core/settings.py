import pygame
import yaml

def tuple_constructor(loader, node):
    return tuple(loader.construct_sequence(node))

yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/tuple', tuple_constructor)

with open("Hashi-dotQ/core/yaml/settings.yaml") as f:
    __data = yaml.safe_load(f)

size = width, height = 800, 500
game_display = pygame.display.set_mode(size)
pygame.display.set_caption('Quantum Hashi')

# colors
c1 = __data["c1"]
c2 = __data["c2"]
c3 = __data["c3"]
c4 = __data["c4"]
c5 = __data["c5"]
c6 = __data["c6"]
c7 = __data["c7"]
c8 = __data["c8"]
c9 = __data["c9"]
text = __data["white"]
black = __data["black"]
max_circle = __data["max_circle"]
green = __data["green"]
bright_green = __data["bright_green"]
dark_green = __data["dark_green"]
blur_green = __data["blur_green"]
circle_green = __data["circle_green"]
cyan = __data["cyan"]
red = __data["red"]

clock = pygame.time.Clock()


def load_file(url):
    bg_img = pygame.image.load(url)
    return pygame.transform.scale(bg_img,(width,height))
