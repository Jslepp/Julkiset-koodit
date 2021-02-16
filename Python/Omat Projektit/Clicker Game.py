import sys
import pygame
from pygame.locals import *
pygame.init()

leveys = 500
korkeus = 500
pinta = pygame.display.set_mode((leveys,korkeus))
pygame.display.set_caption("Klikkaa")

musta = (0,0,0)  
puna = (255,0,0) 
vihr = (0,255,0)  
sini = (0,0,255) 

klikkaus = 0
tupla = 1
tuplaklikkausTotuus = False
autoclicker = False
start_ticks=pygame.time.get_ticks()
i = 1

smallfont = pygame.font.SysFont('Corbel',25)
sammuta = smallfont.render('Sammuta', True , (255,255,255))
klikkaa = smallfont.render('Klikkaa', True , (255,255,255))
tuplaklikkaus = smallfont.render('Tuplaklikkaus: 10', True , (255,255,255))
autoklikkaus = smallfont.render('Autoclicker: 50', True , (255,255,255))
klikit = smallfont.render('Klikkaukset' , True , (255,255,255))
klikitMäärä = smallfont.render(str(klikkaus) , True , (255,255,255))

def buttonCommand():
    global klikkaus
    if tuplaklikkausTotuus == True:
        klikkaus = klikkaus + 2
    else:
        klikkaus = klikkaus + 1

    print(klikkaus, "Klikkausta")
    

def purchaseDoubleClicksCommand():
    global klikkaus
    global tuplaus
    if klikkaus <10:
        print ("Ei tarpeeksi klikkauksia. Vaaditaan vähintään 10 klikkausta tuplaklikkauksen ostamiseen!!!")
    if klikkaus >=10:
        global tuplaklikkausTotuus
        tuplaklikkausTotuus = True

def purchaseAutoClickCommand():
    global klikkaus
    global autoclicker
    if klikkaus > 50:
        autoclicker = True
            


while True:
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if leveys/2 <= mouse[0] <= leveys/2+140 and korkeus/2 <= mouse[1] <= korkeus/2+40: 
                pygame.quit()
            if leveys/2 <= mouse[0] <= leveys/2+140 and korkeus/2-70 <= mouse[1] <= korkeus/2-30:
                buttonCommand()
            if leveys/2 <= mouse[0] <= leveys/2+140 and korkeus/2-140 <= mouse[1] <= korkeus/2-100:
                purchaseDoubleClicksCommand()
            if leveys/2 <= mouse[0] <= leveys/2+140 and korkeus/2-210 <= mouse[1] <= korkeus/2-170:
                purchaseAutoClickCommand()
                
    klikitMäärä = smallfont.render(str(klikkaus) , True , (255,255,255))            

    pinta.fill(musta)            
    mouse = pygame.mouse.get_pos()

    

    #Automaattinenklikkaus
    if leveys/2 <= mouse[0] <= leveys/2+140 and korkeus/2-210 <= mouse[1] <= korkeus/2-170:
        pygame.draw.rect(pinta,(170,170,170),[leveys/2,korkeus/2-210,200,40])
    else:
        pygame.draw.rect(pinta,(100,100,100),[leveys/2,korkeus/2-210,200,40])
    pinta.blit(autoklikkaus , (leveys/2,korkeus/2-210))
    
    #Klikkausnappula
    if leveys/2 <= mouse[0] <= leveys/2+140 and korkeus/2-70 <= mouse[1] <= korkeus/2-30:
        pygame.draw.rect(pinta,(170,170,170),[leveys/2,korkeus/2-70,200,40])
    else:
        pygame.draw.rect(pinta,(100,100,100),[leveys/2,korkeus/2-70,200,40])
    pinta.blit(klikkaa , (leveys/2,korkeus/2-70))

    #Tuplaklikkaus
    if leveys/2 <= mouse[0] <= leveys/2+140 and korkeus/2-140 <= mouse[1] <= korkeus/2-100:
        pygame.draw.rect(pinta,(170,170,170),[leveys/2,korkeus/2-140,200,40])
    else:
        pygame.draw.rect(pinta,(100,100,100),[leveys/2,korkeus/2-140,200,40])
    pinta.blit(tuplaklikkaus , (leveys/2,korkeus/2-140))

    #Sammutusnappula
    if leveys/2 <= mouse[0] <= leveys/2+140 and korkeus/2 <= mouse[1] <= korkeus/2+40:
        pygame.draw.rect(pinta,(170,170,170),[leveys/2,korkeus/2,200,40])
    else:
        pygame.draw.rect(pinta,(100,100,100),[leveys/2,korkeus/2,200,40])
    pinta.blit(sammuta , (leveys/2,korkeus/2))

    #Klikit
    pinta.blit(klikit , (leveys/2-230,korkeus/2-200))
    pinta.blit(klikitMäärä , (leveys/2-110,korkeus/2-200))

    seconds = pygame.time.get_ticks()/1000 #calculate how many seconds

    if int(seconds) == i:
        i = i + 1
        if autoclicker == True:
            klikkaus = klikkaus + 1


    pygame.display.update()
