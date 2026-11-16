import pygame as pg
import random
from Jogador import Jogador
from Bolinha import Bolinha
from Bloco import *
from Pontos import Pontos as pts


def gerarCor():
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    conjCores = (color1, color2, color3)
    return conjCores

def corBlocos(tupla):
    if tupla[0] - 75 > 0:
        color1 = tupla[0] - 75
    elif tupla[0] + 75 < 255:
        color1 = tupla[0] + 75
    else:
        color1 = random.randint(0, 255)

    color2 = tupla[1]
    color3 = tupla[2]
    conjCores = (color1, color2, color3)
    return conjCores

def movimentaJogador(jogador, largura):
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        jogador.move(-jogador.velocidade, largura)
    elif keys[pg.K_RIGHT]:
        jogador.move(jogador.velocidade, largura)

def desenhaCoisas(tela, jogador, bolinha, blocos, estado):

    if estado == 1:
        fonte = pg.font.SysFont("Arial", 90)
        texto = fonte.render("Game Over", True, "red")
        tela.blit(texto, (tela.get_width() // 2 - texto.get_width() // 2, tela.get_height()// 2 - texto.get_height() // 2))
    elif estado == 2:
        fonte = pg.font.SysFont("Arial", 90)
        texto = fonte.render("Você venceu!", True, "green")
        tela.blit(texto, (tela.get_width() // 2 - texto.get_width() // 2, tela.get_height()// 2 - texto.get_height() // 2))
    else:
        tela.fill("black")
        # Chagpt alucinações pra deixar transparente
        retangulo_transp = pg.Surface((900, 15), pg.SRCALPHA) 
        pg.draw.rect(retangulo_transp, (255, 255, 255, 50), (0, 0, 900, 15))
        tela.blit(retangulo_transp, (0, 550))

        pg.draw.rect(tela, jogador.cor, jogador.reta, border_radius=20)
        
        pg.draw.circle(tela, bolinha.cor, bolinha.shape.center, bolinha.tamanho)
        for bloco in blocos.blocos:
            pg.draw.rect(tela, bloco.cor, bloco.shape, border_radius=5)

        fontePts = pg.font.SysFont("Arial", 30, True)
        texto = fontePts.render(f'Pontos: {pts.getPontos()}', True, "White")
        tela.blit(texto, (10, 515))

    pg.display.update()

def moveBola(bola, largura, altura, jogador, blocos):
    if len(blocos.blocos) == 0:
        return 2
    if bola.move(largura, altura, jogador, blocos):
        return 0
    return 1

def iniciarJogo():
    pg.init()

    largura = 900
    altura  = 600
    numeroLinhas = 8
    numeroColunas = 7
    estado = True

    clock = pg.time.Clock()

    tela = pg.display.set_mode((largura, altura))
    novoJogador = Jogador(gerarCor(), 200, 13)
    novoJogador.iniciarJogador(largura, altura)

    novaBolinha = Bolinha("white", 10, 5, 5)
    novaBolinha.criarBola(altura, largura)
    blocos = Blocos(corBlocos(novoJogador.cor))
    blocos.criaBlocos(numeroLinhas, numeroColunas, largura, altura)

    while True:
        
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        desenhaCoisas(tela, novoJogador, novaBolinha, blocos, estado)
        movimentaJogador(novoJogador, largura)
        estado = moveBola(novaBolinha, largura, altura, novoJogador.reta, blocos)


iniciarJogo()

