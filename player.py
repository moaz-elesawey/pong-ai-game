import pygame

from constants import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, WHITE, PADD_VAL


class Player:
    def __init__(self, side, width=PLAYER_WIDTH, height=PLAYER_HEIGHT, color=WHITE):
        self.side = side
        self.width = width
        self.height = height
        self.color = color
        self.x = None
        self.y = HEIGHT // 2

        self.score = 0

        if self.side == 'left':
            self.x = PADD_VAL
        elif self.side == 'right':
            self.x = WIDTH - PLAYER_WIDTH - PADD_VAL
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.width, self.height])

    def move(self):
        if self.y > HEIGHT - self.height:   self.y = HEIGHT - self.height 
        elif self.y < 0: self.y = 0


