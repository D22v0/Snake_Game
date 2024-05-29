import pygame
from sys import exit
from pygame import *
from random import randint


pygame.init()


fonte = pygame.font.SysFont('arial', 40, True, True)
som_c = pygame.mixer.Sound('game_apha/snake_game/bubble_pop.wav')
pontos = 0
# Janela
largura = 1280
altura = 960
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Game.Snake_Apha')
# Pi
x_cobra = largura/2 - 50/2
y_cobra = largura/2 - 50/2

velocidade =10
x_controle = velocidade
y_controle = 0


L_r = 20
A_r = 20

#P do item
x_m = randint(40,800)
y_m = randint(50,630)


relogio = pygame.time.Clock()

# lista de aumento da cobra
T_cobra = []
comprimento_inicial = 5


def aumenta_cobra(T_cobra):
        for xey in T_cobra:
            # xey = [x,y]
            # xey[0] = x
            pygame.draw.rect(tela,(0,255,0),(xey[0],xey[1],20,20))

#game over
morreu = False

def reiniciar():
    global pontos,comprimento_inicial,x_cobra,y_cobra,T_cobra,T_cabeca,x_m,y_m,morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura/2
    y_cobra = altura/2
    T_cobra = []
    T_cabeca = []
    x_m = randint(40,600)
    y_m = randint(50,430)
    morreu = False

while True:
    #variavel de frame
    relogio.tick(30)
    # .fill apaga rastro de eventos
    tela.fill((0,0,0))

    #Criando Texto
    mensagem = f'Pontos: {pontos}'
                        # (Texto, antialising, (cor), )
    texto = fonte.render(mensagem, True, (255,255,255))


    for event in pygame.event.get():
        #Fechar a janela
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
                if event.key == K_a:
                    # if de bloqueio de tecla
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                if event.key == K_d:
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                if event.key == K_w:
                    if y_controle == velocidade:
                        pass
                    else:
                        x_controle = 0
                        y_controle = -velocidade
                if event.key == K_s:
                    if y_controle == -velocidade:
                        pass
                    else:
                        x_controle = 0
                        y_controle = velocidade


   


    x_cobra = x_cobra + x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela, (0,255,0) , (x_cobra,y_cobra,A_r,L_r))
    
    maca = pygame.draw.circle(tela,(255,0,0),(x_m,y_m),(15))

    #Linha                                pi       pF
                    #(tela,   (cor),    (x,y),  (x,y),   (raio) )
    # pygame.draw.line(tela,(150,150,0),(390,0),(390,600),(10))

    # Colisao de objetos
    '''colliderect(), esse metodo verifica a colisao'''
    if cobra.colliderect(maca):                                                                            
        x_m = randint(40,600)
        y_m = randint(50,430)
        #toda vez que pegar a maca, ela aumenta
        comprimento_inicial +=5


        pontos+= 1

        som_c.play()
    T_cabeca = []
    T_cabeca.append(x_cobra)
    T_cabeca.append(y_cobra)

    T_cobra.append(T_cabeca)

    #Game Over
    if T_cobra.count(T_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 25, True, True)
        mensagem = 'Game Over! Pressione a tecla R  para jogar novamente'
        texto = fonte2.render(mensagem,True, (0,0,0))
        ret_texto = texto.get_rect()
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            ret_texto.center = (largura//2,altura//2)
            tela.blit(texto, (ret_texto))
            pygame.display.update()

    # Reaparecer do outro lado
    if x_cobra > largura:
        x_cobra = 0    
    if x_cobra < 0:
        x_cobra = largura

    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0   

    # tamanho da cobra
    if len(T_cobra) > comprimento_inicial:
        del T_cobra[0]

    aumenta_cobra(T_cobra)

    #Colocando e Posicionando o texto na tela
            #(texto, (x,y) )
    tela.blit(texto, (580,60))
    
    # A cada interacao do loop principal, a funcao a baixo atualiza o jogo
    pygame.display.update()