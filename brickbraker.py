import pygame as pg

def inicia_jogo():
    pg.init()

    largura = 800
    altura  = 500

    tela = pg.display.set_mode((largura, altura))

    jogador = Jogador('white', 200, 13)
    jogador.cria_jogador(altura)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        pg.draw.rect(tela, jogador.cor, jogador.jogador)
        pg.display.update()
        
class Jogador:
    def __init__(self, cor, tamanho_barra, velocidade):

        self.cor = cor
        self.velocidade = velocidade
        self.tamanho_barra = tamanho_barra
        self.jogador = None
        
    def cria_jogador(self, altura):
        self.jogador = pg.Rect(350, altura-50, self.tamanho_barra, 15)
    
    
inicia_jogo()
