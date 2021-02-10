import pygame

pygame.font.init()

# constants
WIDTH, HEIGHT = 900, 550
CENTER = WIDTH // 2, HEIGHT // 2
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 140

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_XXBIG = pygame.font.Font('fonts/squada.ttf', 100)
FONT_XBIG = pygame.font.Font('fonts/squada.ttf', 55)
FONT_BIG = pygame.font.Font('fonts/squada.ttf', 35)
FONT_SML = pygame.font.Font('fonts/squada.ttf', 30)
FONT_XSML = pygame.font.Font('fonts/squada.ttf', 10)

FPS = 50
SPEED = 10
PADD_VAL = 10

BALL_RADIUS = 15
BALL_SPEED = 30

