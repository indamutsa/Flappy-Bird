# Imports
import os
import pygame
import random
import time
import neat

# Constants
WIN_WIDTH = 500
WIN_HEIGHT = 800

# Load Images
# Using scale2x to make the images bigger
BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png"))),
]

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))