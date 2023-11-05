import Principal
import Principal2

"""
==============================
Verde = 
Rosa = escolhe a cor
Vermelho = ativar e desativar o desenho
Azul = diminuir e aumentar o canvas
"""

canvas , paleta = Principal.Principal()

newCanvas = Principal2.SuperiorEsquerdo(canvas)

Principal2.draw(newCanvas)
