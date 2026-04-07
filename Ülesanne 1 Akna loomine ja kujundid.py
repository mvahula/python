#Ülesanne 1: Akna loomine ja kujundid

#impordin pygame
import pygame

#panen pygame tööle
pygame.init()

#Tekitan uue akna 300*300
screen = pygame.display.set_mode((300, 300))

#Lisan programmiaknale nime
pygame.display.set_caption("Foor - Vahula")

#teen tausta
screen.fill((10, 10, 15))

#teen punase ringi
pygame.draw.circle(screen, (250, 10, 10), (150, 80), 35)

#teen kollase ringi
pygame.draw.circle(screen, (250, 250, 10), (150, 155), 35)

#teen rohelise ringi
pygame.draw.circle(screen, (10, 250, 10), (150, 230), 35)

#teen seest tühja ristküliku joonte abil
pygame.draw.line(screen, (150, 150, 150), (100, 30), (200, 30), 2)
pygame.draw.line(screen, (150, 150, 150), (100, 30), (100, 275), 2)
pygame.draw.line(screen, (150, 150, 150), (200, 30), (200,275), 2)
pygame.draw.line(screen, (150, 150, 150), (100, 275), (200, 275), 2)

#värskendan pilti
pygame.display.flip()

#teen nii, et programmi saab ilusti kinni panna
tootab = True
while tootab:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tootab = False
pygame.quit()