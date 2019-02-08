import pygame
from pygame.locals import *
from my_functions import randomizer
from my_functions import colour_change
pygame.init()

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

#SCREEN DIMENSION AND BACKGROUND COLOUR
screen=pygame.display.set_mode((640, 480), 0, 32)
screen.fill(BEIGE)


#FILE READING
text_file=open("the_words.txt")
word=[]
for a in text_file:
    word += [a]
word_length=len(word)

word_number=randomizer(word_length)
the_special_word=word[word_number]


#DEFAULT (COLOUR + TIME)
colour=BLACK
playing=True
state=0
word_delay=0
player_number=1
player_delay=0
remaining=10
timer=0

#TEXT
font=pygame.font.Font("Vera.ttf",16)
bigger_font=pygame.font.Font("Vera.ttf", 30)
biggest_font=pygame.font.Font("Vera.ttf",50)
font_bold=pygame.font.Font("VeraBd.ttf",20)
font_small_bold=pygame.font.Font("VeraBd.ttf", 16)

#PICTURES
#http://www.manicgamer.net/wp/wp-content/images/stories/picultimate/2467Pictionary%20Ultimate%20Edition%20Logo.png
logo = pygame.image.load('logo.png')
#http://sp-prod.com/ifa_bo/map/reset.png
restart = pygame.image.load('restart.png')
restart = pygame.transform.scale(restart, (30,30))

'''--------------GAME CODE--------------------------'''
while playing== True:

    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                playing==False

    mouse_position=pygame.mouse.get_pos()

    #MAIN MENU
    if state==0:
        screen.blit(logo, (130,20))
        font=pygame.font.Font("Vera.ttf",16)
        title_surface=font.render("'The Unofficial python game'",True, WATER)
        screen.blit(title_surface,(210,180))
        #Play button
        pygame.draw.rect(screen,WATER, (160,300,320,40))
        play_button=font_bold.render("PLAY GAME",True,WHITE)
        screen.blit(play_button,(260,305))
        start_surface=font.render("Click the play key to start the game", True, GREEN)
        screen.blit(start_surface, (180,230))
        #Instruction button
        pygame.draw.rect(screen,WATER,(160,350,320,40))
        instruction_button=font_bold.render("INSTRUCTIONS",True,WHITE)
        screen.blit(instruction_button,(235,355))
        #Coder/Developer
        author=font.render("Game designed and coded by Gabriel Yeung", True, ORANGE)
        screen.blit(author,((150,430)))

        #Two main menu button
        if pygame.mouse.get_pressed()[0]:
            if mouse_position[0]>160 and mouse_position[0]<480:
                #Play
                if mouse_position[1]>300 and mouse_position[1]<340:
                    screen.fill(BEIGE)
                    state=1
                #Instructions
                if mouse_position[1]>350 and mouse_position[1]<390:
                    screen.fill(BEIGE)
                    state=3

        pygame.display.update()

    if state==1:
        #Determining if it's player 1 or player 2
        if player_number%2==0:
            player="2"
        else:
            player="1"

        #Displays which player's turn it is /alternates
        if player_delay<720:
            screen.blit(logo, (115,0))
            player_surface=biggest_font.render("Team "+player+"'s turn", True, BLUE)
            screen.blit(player_surface, (145,200))
            other_player_surface=bigger_font.render("Same team members look away!", True, WATER)
            screen.blit(other_player_surface, (75, 255))
            player_delay+=1
        else:
            screen.fill(BEIGE)
            #Holds screen for 5 seconds
            if word_delay<600:
                screen.blit(logo, (115,0))
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

    if state==2:
        screen.blit(logo, (115,0))
        #Timer
        if timer<7200:
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
            elif keys[pygame.K_r]:
                screen.fill(BEIGE)
                word_number=randomizer(word_length)
                the_special_word=word[word_number]
                state=1
                word_delay=0
                player_delay=0
                screen.fill(BEIGE)
                player_number+=1
                timer=0
                remaining=10

            elif keys[pygame.K_s]:
                pygame.image.save(screen,"latest_drawing.jpg")

            #Left clicks
            if pygame.mouse.get_pressed()[0]:
                #Check mouse position to determine what to do. Draw or change colour.
                if mouse_position[0]>600 and mouse_position[0]<620 and mouse_position[1]>120 and mouse_position[1]<390.76:
                    colour=colour_change(mouse_position)
                elif mouse_position[0]>600 and mouse_position[0]<630 and mouse_position[1]>10 and mouse_position[1]<40:
                    screen.fill(BEIGE)
                    word_number=randomizer(word_length)
                    the_special_word=word[word_number]
                    state=1
                    word_delay=0
                    player_delay=0
                    screen.fill(BEIGE)
                    player_number+=1
                    colour=BLACK
                    timer=0
                    remaining=10

                else:
                    pygame.draw.circle(screen,colour,(mouse_position),5)

            #Right click --> to erase
            if pygame.mouse.get_pressed()[2]:
               pygame.draw.circle(screen,BEIGE,(mouse_position),10)

            #Restart icon
            screen.blit(restart, (595,10))

            #90 seconds + bar
            timer+=1
            remaining+=0.04
        else:
            #Display gameover for 5 seconds
            if timer<7800:
                screen.fill(BEIGE)
                screen.blit(logo, (115,0))
                game_over=bigger_font.render("TIME IS UP!", True, RED)
                screen.blit(game_over, (200,230))
                restart_game=font.render("Game will restart in 5 seconds!", True, GREEN)
                screen.blit(restart_game, (190,270))
                timer+=1
            #Restart round
            else:
                screen.fill(BEIGE)
                word_number=randomizer(word_length)
                the_special_word=word[word_number]
                state=1
                word_delay=0
                player_delay=0
                screen.fill(BEIGE)
                player_number+=1
                colour=BLACK
                timer=0
                remaining=10

    #INSTRUCTIONS
    if state==3:
        screen.blit(logo, (115,0))
        #Text
        rule_title=bigger_font.render("INSTRUCTIONS/RULES", True, BLUE)
        rule_d=font.render("-Change colour by click the colored squares", True, WATER)
        rule_a=font.render("-Divide amongst two teams", True, WATER)
        rule_b=font.render("-One team members draws the given word", True, WATER)
        rule_c=font.render("-Other members have to guess their drawing", True, WATER)
        rule_e=font.render("-Once correct, click the top right button", True, WATER)
        rule_f=font.render("-Left click to draw and right click to erase", True, WATER)
        rule_h=font.render("-The box under the colour bar indicates the current colour", True, WATER)
        rule_i=font.render("-ROUND WILL AUTO END IN 60 SECONDS", True, RED)
        rule_j=font.render("-Press the 's' key to save current drawing.", True, WATER)

        #Render text
        screen.blit(rule_title, (140,160))
        screen.blit(rule_a,(100,200))
        screen.blit(rule_b,(100,220))
        screen.blit(rule_c,(100,240))
        screen.blit(rule_d,(100,260))
        screen.blit(rule_f,(100,280))
        screen.blit(rule_h,(100,300))
        screen.blit(rule_e,(100,320))
        screen.blit(rule_j,(100,340))
        screen.blit(rule_i,(100,360))

        #Arrow drawings (body + tip)
        pygame.draw.rect(screen,WATER, (60,400,120,30))
        pygame.draw.rect(screen,WATER,(460,400,120,30))
        pygame.draw.polygon(screen,WATER,[[40,415],[70,390],[70,440]])
        pygame.draw.polygon(screen,WATER,[[600,415],[570,390],[570,440]])

        #Text on arrows
        rules_forward=font_small_bold.render("PLAY", True, WHITE)
        rules_back=font_small_bold.render("GO BACK", True, WHITE)
        screen.blit(rules_forward, (500,405))
        screen.blit(rules_back, (90,405))

        if pygame.mouse.get_pressed()[0]:
            if mouse_position[1]>390 and mouse_position[1]<440:
                if mouse_position[0]>40 and mouse_position[0]<180:
                    screen.fill(BEIGE)
                    state=0
                if mouse_position[0]>460 and mouse_position[0]<600:
                    screen.fill(BEIGE)
                    state=1
        timer+=1

    my_clock.tick(120) #120 FPS

    pygame.display.update()

pygame_quit()
