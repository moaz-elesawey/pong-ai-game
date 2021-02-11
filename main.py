import pygame
import random

from constants import *
from player import Player
from ball import Ball
from text import render_text
from model import test

import time
import pickle


pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong Game')

player1 = Player(side='left')
player2 = Player(side='right')

ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS, WHITE)

data = {'ball': [], 'player1_y': [], 'player2_y': []}
trained_model = './models/[1613035926]-model.pkl'


def main(train=False):
    run = True
    clock = pygame.time.Clock()
    started = False
    player_win = False
    which_player =  0
    replay = False


    def draw(win):

        win.fill(BLACK)
        if started:
            player2.draw(win)
            player1.draw(win)

            player1.move()
            player2.move()

            ball.draw(win)
            ball.move()

            win.blit(*render_text('PLAYER 1', WIDTH // 4, 22, FONT_BIG))
            win.blit(*render_text('PLAYER 2', WIDTH - (WIDTH // 4), 22, FONT_BIG))
            
            win.blit(*render_text('{}'.format(player1.score ), WIDTH // 4, 62, FONT_SML))
            win.blit(*render_text('{}'.format(player2.score), WIDTH - (WIDTH // 4), 62, FONT_SML))
            
            # draw the separate line
            for i in range(0, HEIGHT, 10):
                pygame.draw.rect(win, WHITE, [(WIDTH // 2) - 1, i, 2, 7])

        else:
            win.blit(*render_text('AI PING PONG GAME', WIDTH // 2, HEIGHT // 3, FONT_XXBIG))
            win.blit(*render_text('PRESS SPACE OR RETURN TO START THE GAME', WIDTH // 2, HEIGHT - (HEIGHT // 3), FONT_BIG))

        if player_win:
            ball.move_val_x = 0
            ball.move_val_y = 0
            ball.x, ball.y = CENTER 

            win.blit(*render_text('GAME OVER', WIDTH // 2, HEIGHT // 5, FONT_XBIG))
            win.blit(*render_text('PLAYER {} WINS'.format(which_player), WIDTH // 2, HEIGHT // 3, FONT_XBIG))

            win.blit(*render_text('PRESS SPACE OR RETURN TO START THE GAME', WIDTH // 2, HEIGHT - (HEIGHT // 3), FONT_BIG))
         
        pygame.display.update()

    while run:
        
        keys = pygame.key.get_pressed()

        clock.tick(FPS)
        draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return 

        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
            started = True

        if player1.score == 6 or player2.score == 6:
            if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                replay = True
                player_win = False
                which_player = 0
                player1.score = 0
                player2.score = 0

                ball.move_val_x = BALL_SPEED
                ball.move_val_y = BALL_SPEED

        if started:

            data['ball'].append([ball.y, ball.x])

            data['player1_y'].append(player1.y)
            data['player2_y'].append(player2.y)

            # check for the collisions
            if ball.y in range(player1.y, player1.y+PLAYER_HEIGHT) and ball.x <= PLAYER_WIDTH+PADD_VAL+BALL_RADIUS:
                ball.move_val_x *= -1

            if ball.y in range(player2.y, player2.y+PLAYER_HEIGHT) and ball.x >= WIDTH - (PLAYER_WIDTH+PADD_VAL+BALL_RADIUS):
                ball.move_val_x *= -1

            # check for the score change
            if ball.x < 0:
                player2.score += 1
                ball.x, ball.y = CENTER 

            if ball.x > WIDTH:
                player1.score += 1
                ball.x, ball.y = CENTER 

            # check for the winning
            if player1.score >= 6:
                player_win = True
                which_player = 1

            elif player2.score >= 6:
                player_win = True
                which_player = 2
            if train:
                # left player
                # player1.y = test([ball.y], './models/[1612961767]-model-best.pkl')
                if keys[pygame.K_w]:
                    player1.y -= SPEED 
                if keys[pygame.K_s]:
                    player1.y += SPEED

                # right player
                if keys[pygame.K_UP]:
                    player2.y -= SPEED
                if keys[pygame.K_DOWN]:
                    player2.y += SPEED

            else:
                # ai player1
                player1.y = test([ball.y, ball.x], trained_model)

                # ai player2
                # player2.y = test([ball.y, ball.x], trained_model)
                if keys[pygame.K_UP]:
                    player2.y -= SPEED
                if keys[pygame.K_DOWN]:
                    player2.y += SPEED


    pygame.display.update()

if __name__ == '__main__':
    main(train=False)
    
    with open(f'./data/[{int(time.time())}]-data.pkl', 'wb') as f:
        pickle.dump(data, f)

