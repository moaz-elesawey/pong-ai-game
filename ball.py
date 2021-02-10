import pygame
import random
from constants import BALL_SPEED, HEIGHT, WIDTH


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

        __direction = random.choice([-1, 1])

        self.move_val_x = __direction*BALL_SPEED
        self.move_val_y = __direction*BALL_SPEED

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.move_val_x
        self.y += self.move_val_y

        # if self.x >= WIDTH - self.radius: self.move_val_x = -BALL_SPEED
        # elif self.x <= self.radius:   self.move_val_x =  BALL_SPEED

        if self.y >= HEIGHT - self.radius: self.move_val_y = -BALL_SPEED
        elif self.y <= self.radius:    self.move_val_y =  BALL_SPEED


