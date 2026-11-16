import pygame as pg

class Jogador:
    def __init__(self, cor, tamanho, velocidade):
        self.cor = cor
        self.tamanho = tamanho
        self.velocidade = velocidade
        self.reta = None

    def iniciarJogador(self, largura, altura):
        self.reta = pg.Rect(largura / 2, altura - 50, self.tamanho, 15)

    def move(self, vel, largura):
        self.reta.x += vel

        if self.reta.x < 0:
            self.reta.x = 0
        elif self.reta.x > largura - self.tamanho:
            self.reta.x = largura - self.tamanho

