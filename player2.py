import pygame
import random
import time
import socket, sys
from pygame.locals import *

#Other_ip = '10.220.226.67'
#port_number = 5000
HOST = '10.220.226.67'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))


pygame.init()

screen=pygame.display.set_mode((640, 480), 0, 32)

#textbox class
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
boxfont = pygame.font.Font('Vera.ttf', 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = boxfont.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = boxfont.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

#end of textbox class


#COLOUR VARIABLES. Some colour tuple taken with permission from DANIEL PANG
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
LIME=(0,255,0)
BLUE=(50,50,225)
GREEN=(0,128,0)
AQUA=(0,255,255)
WATER=(100,149,237)
FUCHSIA=(255,0,255)
PURPLE=(128,0,128)
YELLOW=(255,255,0)
ORANGE=(255,102,0)
BEIGE=(245,241,222)
BROWN=(139,69,19)
my_clock=pygame.time.Clock()

screen.fill(BEIGE)

colour=BLACK
playing=True
state=0
word_delay=0
player_number=1
player_delay=0
remaining=10
timer=0
logo = pygame.image.load('logo.jpg')
restart = pygame.image.load('restart.png')
winner = pygame.image.load('winner.png')
restart = pygame.transform.scale(restart, (30,30))


#colour changing
def colour_change(mouse_position):
    if mouse_position[1]<140.83:
        colour=RED
        return colour
    elif mouse_position[1]<161.66:
        colour=FUCHSIA
        return colour
    elif mouse_position[1]<182.49:
        colour=PURPLE
        return colour
    elif mouse_position[1]<203.32:
        colour=BLUE
        return colour
    elif mouse_position[1]<224.15:
        colour=AQUA
        return colour
    elif mouse_position[1]<244.98:
        colour=WATER
        return colour
    elif mouse_position[1]<265.81:
        colour=GREEN
        return colour
    elif mouse_position[1]<286.64:
        colour=LIME
        return colour
    elif mouse_position[1]<307.47:
        colour=YELLOW
        return colour
    elif mouse_position[1]<328.3:
        colour=ORANGE
        return colour
    elif mouse_position[1]<349.13:
        colour=BROWN
        return colour
    elif mouse_position[1]<369.93:
        colour=BLACK
        return colour
    else:
        colour=WHITE
        return colour


#TEXT
font=pygame.font.Font("Vera.ttf",16)
bigger_font=pygame.font.Font("Vera.ttf", 30)
biggest_font=pygame.font.Font("Vera.ttf",50)
font_bold=pygame.font.Font("VeraBd.ttf",20)
font_small_bold=pygame.font.Font("VeraBd.ttf", 16)

#FILE READING
text_file=open("the_words.txt")
word=[]
for a in text_file:
    word += [a]
word_length=len(word)

word_number=random.randint(0,word_length-1)
the_special_word=word[word_number]

team1score = 0
team2score = 0

while playing== True:

    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                playing==False

    mouse_position=pygame.mouse.get_pos()

    #MAIN MENU
    if state==0:
        screen.blit(logo, (0,0))
        font=pygame.font.Font("Vera.ttf",16)
        title_surface=font.render("'The Unofficial python game'",True, WATER)
        screen.blit(title_surface,(210,180))
        #Play button
        pygame.draw.rect(screen,WATER, (160,300,320,40))
        play_button=font_bold.render("PLAY GAME",True,WHITE)
        screen.blit(play_button,(260,305))
        start_surface=font.render("Click the play key to start the game", True, GREEN)
        screen.blit(start_surface, (180,230))

        if pygame.mouse.get_pressed()[0]:
            if mouse_position[0]>160 and mouse_position[0]<480:
                #Play
                if mouse_position[1]>300 and mouse_position[1]<340:
                    screen.fill(BEIGE)
                    state=1

        pygame.display.update()

    if state==1:
        #Determining if it's player 1 or player 2
        if player_number%2==0:
            state = 1
            #receive word
        else:
            state = 3
            #send word over

        #Displays which player's turn it is /alternates
        #socket send word to opponent
        if player_delay<450:
            screen.blit(logo, (0,0))
            player_surface=biggest_font.render("Your team's turn", True, BLUE)
            screen.blit(player_surface, (145,200))
            other_player_surface=bigger_font.render("Get ready to draw a word!", True, WATER)
            screen.blit(other_player_surface, (145, 255))
            player_delay+=1
        else:
            screen.fill(BEIGE)
            #Holds screen for 5 seconds
            if word_delay<450:
                #screen.blit(logo, (0,0))
                #Prints out the word to draw for 5 seconds
                word_surface=font.render("Draw this:",True, WATER)
                screen.blit(word_surface,(230,150))

                draw_it=bigger_font.render(the_special_word.strip(),True,BLUE)
                screen.blit(draw_it, (240, 170))
                word_delay+=1

            else:
                screen.fill(BEIGE)
                state=2

        pygame.display.update()

    if state==2 :
        #screen.blit(logo, (0,0))
        #Timer
        if timer<600:
            pygame.draw.rect(screen, LIME, (180,420,remaining,20))

            #Colour Bar/Tool Rectangles
            pygame.draw.rect(screen, BLACK, (600,120,20,270.76))
            pygame.draw.rect(screen, RED, (600,120,20,20.83))
            pygame.draw.rect(screen, FUCHSIA, (600, 140.83,20,20.83))
            pygame.draw.rect(screen, PURPLE, (600, 161.66,20,20.83))
            pygame.draw.rect(screen, BLUE, (600, 182.49,20,20.83))
            pygame.draw.rect(screen, AQUA, (600, 203.32,20,20.83))
            pygame.draw.rect(screen, WATER, (600, 224.15,20,20.83))
            pygame.draw.rect(screen, GREEN, (600, 244.98,20,20.83))
            pygame.draw.rect(screen, LIME, (600, 265.81,20,20.83))
            pygame.draw.rect(screen, YELLOW, (600, 286.64,20,20.83))
            pygame.draw.rect(screen, ORANGE, (600, 307.47,20,20.83))
            pygame.draw.rect(screen, BROWN, (600, 328.3,20,20.83))
            pygame.draw.rect(screen, BLACK, (600, 349.13,20,20.83))
            pygame.draw.rect(screen, WHITE, (600, 369.93,20,20.83))

            #Current Colour Box
            pygame.draw.rect(screen, colour, (600,400,20,20.83))

            #Checks to see what keys are being pressed. Corresponding Action
            keys=pygame.key.get_pressed()
            #hot keys colour changing
            if keys[pygame.K_1]:
                colour=BLUE
            elif keys[pygame.K_2]:
                colour=RED
            elif keys[pygame.K_3]:
                colour=GREEN
            elif keys[pygame.K_4]:
                colour=BLACK
            elif keys[pygame.K_5]:
                colour=AQUA
            elif keys[pygame.K_6]:
                colour=WATER
            elif keys[pygame.K_7]:
                colour=FUCHSIA
            elif keys[pygame.K_8]:
                colour=PURPLE
            elif keys[pygame.K_9]:
                colour=YELLOW
            elif keys[pygame.K_0]:
                colour=ORANGE


            elif keys[pygame.K_s]:
                pygame.image.save(screen,"latest_drawing.jpg")

            #Left clicks
            if pygame.mouse.get_pressed()[0]:
                #Check mouse position to determine what to do. Draw or change colour.
                if mouse_position[0]>600 and mouse_position[0]<620 and mouse_position[1]>120 and mouse_position[1]<390.76:
                    colour=colour_change(mouse_position)
                elif mouse_position[0]>600 and mouse_position[0]<630 and mouse_position[1]>10 and mouse_position[1]<40:
                    screen.fill(BEIGE)
                    #word_number=random.randint(0,word_length-1)
                    #the_special_word=word[word_number]
                    state=1
                    word_delay=0
                    player_delay=0
                    screen.fill(BEIGE)
                    #player_number+=1
                    colour=BLACK
                    timer=0
                    remaining=10

                else:
                    pygame.draw.circle(screen,colour,(mouse_position),5)
                    #send data here

            #Right click --> to erase
            if pygame.mouse.get_pressed()[2]:
               pygame.draw.circle(screen,BEIGE,(mouse_position),10)
                #send data here

            #Restart icon
            screen.blit(restart, (595,10))

            #90 seconds + bar
            timer+=1
            remaining+=0.02
        else:
            #Display gameover for 5 seconds
            if timer<7800:
                #screen.fill(BEIGE)
                #screen.blit(logo, (0,0))
                game_over=bigger_font.render("TIME IS UP!", True, RED)
                screen.blit(game_over, (200,230))
                restart_game=font.render("Other team's turn!", True, GREEN)
                screen.blit(restart_game, (190,270))
                score1tracker=font.render("your score: "+ str(team1score),True, GREEN)
                screen.blit(score1tracker, (180,300))
                score2tracker=font.render("their score: "+ str(team2score),True, GREEN)
                screen.blit(score2tracker, (180,330))
                timer+=1
            #Restart round
            else:
                screen.fill(BEIGE)
                word_number=random.randint(0,word_length-1)
                the_special_word=word[word_number]
                state=1
                word_delay=0
                player_delay=0
                screen.fill(BEIGE)
                player_number+=1
                colour=BLACK
                timer=0
                remaining=10
    if state == 3:

        screen.fill(BEIGE)
        input_box= InputBox(200,200,140,32)
        #input_boxes = [input_box]
        if timer<13500:
            '''
            taka við orði
            Hlusta eftir teikningunni
            fær orðið frá teiknara
            textabox compares answers
            breytir state ef rétt gisk
            '''




            '''
            input_box1 = InputBox(100, 100, 140, 32)
            input_box2 = InputBox(100, 300, 140, 32)
            input_boxes = [input_box1, input_box2]
            done = False

            while timer<45:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    for box in input_boxes:
                        box.handle_event(event)

                for box in input_boxes:
                    box.update()

                screen.fill((30, 30, 30))
                for box in input_boxes:
                    box.draw(screen)

                pygame.display.flip()
                time.sleep(1)
                timer+=1
            '''
    if state == 4:
        if player_number%2==0:
            team2score+=1
        else:
            team1score+=1
        if timer<750:
                screen.fill(BEIGE)
                screen.blit(winner, (0,0))
                game_over=bigger_font.render("Correct Guess", True, RED)
                screen.blit(game_over, (200,230))
                restart_game=font.render("Other team's turn!", True, GREEN)
                screen.blit(restart_game, (190,270))
                score1tracker=font.render("your score: "+ str(team1score),True, GREEN)
                screen.blit(score1tracker, (180,300))
                score2tracker=font.render("their score: "+ str(team2score),True, GREEN)
                screen.blit(score2tracker, (180,330))
                timer+=1
            #Restart round
        else:
            screen.fill(BEIGE)
            word_number=random.randint(0,word_length-1)
            the_special_word=word[word_number]
            state=1
            word_delay=0
            player_delay=0
            screen.fill(BEIGE)
            player_number+=1
            colour=BLACK
            timer=0
            remaining=10
    my_clock.tick(300) #120 FPS

    pygame.display.update()

pygame.QUIT()
