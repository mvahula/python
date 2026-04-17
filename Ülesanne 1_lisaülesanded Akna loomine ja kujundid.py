#Ülesanne 1_lisaülesanded: Akna loomine ja kujundid

#Võtan koodi Ülesanne 1-st.

import pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - Vahula")
screen.fill((10, 10, 15))

#Teen valgusfoori väiksemaks ja panen ülespoole, et post ära mahuks
pygame.draw.circle(screen, (250, 10, 10), (150, 60), 20)
pygame.draw.circle(screen, (250, 250, 10), (150, 105), 20)
pygame.draw.circle(screen, (10, 250, 10), (150, 150), 20)

pygame.draw.line(screen, (150, 150, 150), (120, 30), (180, 30), 2)
pygame.draw.line(screen, (150, 150, 150), (120, 30), (120, 180), 2)
pygame.draw.line(screen, (150, 150, 150), (180, 30), (180,180), 2)
pygame.draw.line(screen, (150, 150, 150), (120, 180), (180, 180), 2)

#Lisan posti
pygame.draw.rect(screen, (150, 150, 150), (147, 180, 7, 40))

#Lisan postialuse
#Kuna see koosneb 3-st värvist, siis loon postialuse 3-st erinevast kujundist.
pygame.draw.polygon(screen, (20, 20, 230), [(147, 220), (153, 220), (173, 240), (127, 240)])
pygame.draw.polygon(screen, (0, 0, 0), [(127, 240), (173, 240), (193, 260), (107, 260)])
pygame.draw.polygon(screen, (255, 255, 255), [(107, 260), (193, 260), (213, 280), (87, 280)])

#teen neile joone ümber, et oleks paremini näha.
pygame.draw.line(screen, (150, 150, 150), (147, 220), (87, 280), 2)
pygame.draw.line(screen, (150, 150, 150), (87, 280), (213, 280), 2)
pygame.draw.line(screen, (150, 150, 150), (153, 220), (213, 280), 2)
pygame.draw.line(screen, (150, 150, 150), (147, 220), (153, 220), 2)

pygame.display.flip()

tootab = True
while tootab:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tootab = False
pygame.quit()