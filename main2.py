import pygame

canvas = [[1,2,3],
          [4,7,6],
          [(0,0,0),(0,0,255),(255,0,0),(255,255,0),(0,255,0)]]

canvas2 = [[1,2],
          [(0,0,255),(255,0,0),(255,255,0),(0,255,0)]]

fps = 60
timer = pygame.time.Clock()
largura = 800
altura = 500

branco = (255, 255, 255)

def canvasToCross(canv):
    contador = 0
    perlerV1 = []    
    linhas = len(canv)-1
    colunas = len(canv[0])
    for c in range(linhas):
        for i in range(colunas):
            for p in range(9):
                perlerV1.append(contador)
                contador = contador + 1


    for c in range(linhas):
        for i in range(3):
            for p in range(colunas):
                for t in range(3):
                    pos = ((3*i)+(3*(3*p)) + t) + (c*3*9)
                    perlerV1[pos] = canv[c][p]
    


    for c in range(linhas):
        for i in range(3):
            for p in range(colunas):
                for t in range(3):
                    pos = ((3*i)+(3*(3*p)) + t) + (c*3*9)
                    print(perlerV1[pos], end=' ')
                print('   ', end = '')
            print()
        print()

        

    return perlerV1    


def drawCross(tela, canv):
    linhas = len(canv)-1
    colunas = len(canv[0])

    num = 0

    for c in range(linhas):
        for i in range(3):
            for p in range(colunas):
                for t in range(3):
                    print((3*i)+(3*(3*p)) + t, end=' ')
                print('   ', end = '')
            print()
        print()


aa = canvasToCross(canvas)



