import pygame
import random
import sys
import time
# from button import Button

# Inicializácia Pygame
pygame.init()

# Veľkosť okna hry
screen = DISPLAY = pygame.display.set_mode((700,525),0,32)
DISPLAY = pygame.display 
pygame.display.set_caption('Snakey')
message_to_screen = pygame.font.Font('font.otf', 100)

class Icon: 
    def __init__(self):
        self.sprite = pygame.image.load('icon.png') 

pygame.display.set_icon(Icon().sprite)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
lightpink = (255, 174, 185, 255)
lightpink2 = (139, 95, 101, 255)
# Values ​​for the snake
block_size = 25
snake_speed = 10

# Loading pictures
head_img = pygame.image.load('head.png')  
body = pygame.image.load('body.png')  
apple = pygame.image.load('apple.png')  
icon = pygame.image.load('icon.png')
backgr = pygame.image.load('background.png')
backgr1 = pygame.image.load('title_screen.png')
backgr_dead = pygame.image.load('background_dead.png')

# generating snake
def snake(snake_list,head):
    screen.blit(head, (snake_list[0][0], snake_list[0][1]))
    for segment in snake_list[1:]:
        screen.blit(body, (segment[0], segment[1]))
# generating apple
def generate_apple(snake_list):
        while True:
            randAppleX = round(random.randrange(0, 660) / block_size) * block_size
            randAppleY = round(random.randrange(0, 485) / block_size) * block_size
            if [randAppleX, randAppleY] not in snake_list:
                break
        return randAppleX, randAppleY

# Drawing messages on screen
def message_from(msg,color):
    font = pygame.font.Font('font.otf', 30)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, ([155, 215]))
def message_splash_screen(msg, color): 
    font = pygame.font.Font('font.otf', 75)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, ([210, 220]))
def message_title_screen(msg,color):
    font = pygame.font.Font('slkscrb.ttf', 100)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, ([100, 220])) 
def message_death(msg, color):
    font = pygame.font.Font('slkscrb.ttf', 100)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, ([50, 180]))
def message_death1(msg, color):
    font = pygame.font.Font('slkscrb.ttf', 20)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, ([120, 290])) 
def message_play(msg,color):
    font = pygame.font.Font('slkscrb.ttf', 20)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, ([90, 320])) 
# Splashscreen 
splashScreen = True
while splashScreen: 
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    splashScreen = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    if splashScreen == True:
        screen.fill(lightpink)
        message_splash_screen("FRANCESKO", lightpink2)
        message_from("from", lightpink2)
        pygame.display.update()
        pygame.time.delay(10)
        splashScreen = pygame.time.wait(3000)
        splashScreen = False

# Titlescreen 
titleScreen = True 
while titleScreen: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                titleScreen = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
    screen.fill(white)
    screen.blit(backgr1, (0,0))
    message_title_screen("SNAKEY", lightpink2)
    message_play(">> PRESS SPACE TO START THE GAME <<", black)
    pygame.display.update()
    pygame.time.delay(10)

# main game loop
def gameLoop():
    game_over = False
    game_close = False
    snake_speed = 5
    lead_x = 350
    lead_y = 250
    lead_x_change = 0
    lead_y_change = 0
    head = head_img
    snake_list = [[lead_x, lead_y]]
    snake_length = 1
    score = 0
        
    randAppleX, randAppleY = generate_apple(snake_list)
    
    
    while not game_over:
        
        while game_close == True:
            screen.fill(white)
            screen.blit(backgr_dead, (0, 0))
            message_death("YOU DIED", black)
            message_death1(">> PRESS SPACE TO PLAY AGAIN <<", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change != block_size:
                    lead_x_change = - block_size
                    lead_y_change = 0
                    head = pygame.transform.rotate(head_img, 90)
                if event.key == pygame.K_RIGHT and lead_x_change != - block_size:
                    lead_x_change = block_size
                    lead_y_change = 0
                    head = pygame.transform.rotate(head_img, -90)
                elif event.key == pygame.K_UP and lead_y_change != block_size:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    head = pygame.transform.rotate(head_img, 0)
                elif event.key == pygame.K_DOWN and lead_y_change != - block_size:
                    lead_y_change = block_size
                    lead_x_change = 0
                    head = pygame.transform.rotate(head_img, 180)
                elif event.key == pygame.K_a and lead_x_change != block_size:
                    lead_x_change = - block_size
                    lead_y_change = 0
                    head = pygame.transform.rotate(head_img, 90)
                elif event.key == pygame.K_d and lead_x_change != - block_size:
                    lead_x_change = block_size
                    lead_y_change = 0
                    head = pygame.transform.rotate(head_img, -90)
                elif event.key == pygame.K_w and lead_y_change != block_size:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    head = pygame.transform.rotate(head_img, 0)
                elif event.key == pygame.K_s and lead_y_change != - block_size:
                    lead_y_change = block_size
                    lead_x_change = 0
                    head = pygame.transform.rotate(head_img, 180)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    snake_speed += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    pygame.time.Clock().tick(15)

        lead_x += lead_x_change
        lead_y += lead_y_change

        snake_head = [lead_x, lead_y]
        snake_list.insert(0, snake_head)
        
        if len(snake_list) > snake_length:
            snake_list.pop()
        
        for segment in snake_list[1:]:
            if segment == snake_head:
                game_close = True
        
# Checking for colisons
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX, randAppleY = generate_apple(snake_list) 
            snake_length += 1
            score +=1 
            
        if lead_x < 0:
            game_close = True
            lead_x_change = 0
            snake_speed = 0
        if lead_x > 670:
            lead_x_change = 0
            snake_speed = 0
            game_close = True
        if lead_y > 495:
            game_close = True
            lead_y_change = 0
            snake_speed = 0
        if lead_y < 0:
            game_close = True
            lead_y_change = 0
            snake_speed = 0

        def message_score( color, font):
            font = pygame.font.Font('slkscrb.ttf', 30)
            screen_text = font.render("SCORE:" + str(score), True, color)
            screen.blit(screen_text, ([15, 15]))
            
        screen.fill(white)
        screen.blit(backgr, (0, 0))
        screen.blit(apple, (randAppleX, randAppleY ))
        snake(snake_list, head)
        message_score( black, 'slkscrb.ttf')
        
        pygame.display.update()
        pygame.time.Clock().tick(10)

    pygame.quit()
    quit()

gameLoop()