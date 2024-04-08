import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice

pygame.init()



fonte = pygame.font.SysFont('arial',40,bold=True,italic=True)

#Diferença de 160 entre largura e altura
largura = 780
altura = 620
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((780,620))
pygame.display.set_caption("pong")

#Valores Originais 150 - 468
xraquete = 350
yraquete = 568

#Posição da Bolinha
x = 350
y = 568
#-------------#
#Direção da Bolinha
Direita = True
Subir = True
#-------------#

velocidade = 10
pontos = 0

# Função para gerar as barras com cores diferentes
def gerar_barras():
    barras = []
    cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]  # Lista de cores
    for i in range(5):
        cor = choice(cores)  # Escolha uma cor aleatória da lista de cores
        barras.append((pygame.Rect(50 + i * 150, 100, 100, 20), cor))  # Adicione a cor à barra
    return barras

# Inicializa as barras com cores diferentes
barras = gerar_barras()



#Atualizar a tela
while True:
    relogio.tick(15)
    tela.fill((255,255,255))
    mensagem=f"Pontuação.: {pontos}"
    texto_formatado = fonte.render(mensagem, True,(0,0,0,0) )
    tela.blit(texto_formatado,(largura/2, altura/2))

    for barra, cor in barras:
        pygame.draw.rect(tela, cor, barra)

    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_a]:
            xraquete = xraquete - 30
        elif pygame.key.get_pressed()[K_l]:
            xraquete = xraquete + 30
    if xraquete + 100 >largura:
        xraquete = largura - 100
    elif xraquete < 0 :
        xraquete = 0
    if not Subir:
        y = y + velocidade
    else:
        y = y - velocidade
    if not Direita:
        x = x + velocidade
    else:
        x = x - velocidade
    if x > largura:
        Direita = not Direita
    elif x < 0:
        Direita = not Direita
    if y > altura:
        mensagem = "YOU FAIL!"
        exit()
    if(y < 0):
        Subir = not Subir


    # Modifique o desenho da raquete para um objeto Rect
    raquete = pygame.Rect(xraquete, yraquete, 100, 12)
    pygame.draw.rect(tela, (255, 0, 0), raquete)


    bola=pygame.draw.circle(tela,(0,0,255),(x,y),10)

    if bola.colliderect(raquete):
        Subir = not Subir

        if Direita:
            x = x + randint(0,25)
        else:
            x = x - randint(0,25)

    for barra, _ in barras:
        if bola.colliderect(barra):
            barras.remove((barra, _))  # Remova a tupla completa, que contém o objeto Rect e a cor
            pontos += 1                # Incrementa a pontuação
            Subir = not Subir          # Inverte a direção da bola verticalmente
            break

    # Se todas as barras foram destruídas, gere novas barras
    
    if not barras:
        barras = gerar_barras()
    pygame.display.update()