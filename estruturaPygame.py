import time
import pygame

"""
==========================
estrutura basica para pygame
"""

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FUNDO = (169, 169, 169)

# inicia o pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
    

# preenchendo o fundo com preto
screen.fill(FUNDO)


# area de funcoes
def criarSqurt(x, y, tam):
    pygame.draw.rect(screen, COR, [x, y, tam, tam])


# desenhando na superfície
pygame.draw.line(screen, WHITE, [10, 100], [630, 100], 5)
pygame.draw.rect(screen, BLUE, [200, 210, 40, 20])
pygame.draw.ellipse(screen, RED, [300, 200, 40, 60])
pygame.draw.polygon(screen, GREEN, [[420, 200], [440, 240], [400, 240]])




# criando um canvas pixel art
tamanho = 50
COR = (105,89,205)

pygame.draw.rect(screen, COR, [50, 50, tamanho, tamanho])
criarSqurt(50, 105, 50)



# atualizando a tela
pygame.display.flip()
time.sleep(5)




















