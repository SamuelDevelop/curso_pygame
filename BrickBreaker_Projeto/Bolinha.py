# Bolinha.py

import pygame as pg
import random as rd
from Pontos import Pontos as pts

class Bolinha:
    def __init__(self, cor, tamanho, velX, velY):
        self.cor = cor
        self.tamanho = tamanho
        self.velX = velX
        self.velY = velY
        self.vel = [velX, - velY]
        self.contador = 0
        self.posicao = (0, 0)
        self.shape = None

    def criarBola(self, altura, largura):
        self.posicao = (rd.randint(0, largura-self.tamanho), altura * 0.75)
        self.shape = pg.Rect(self.posicao[0], self.posicao[1], self.tamanho, self.tamanho)

    def move(self, largura, altura, jogador, blocos):
        self.shape.x += self.vel[0]
        self.shape.y += self.vel[1]
        self.confereColisaoJogador(jogador)
        self.confereColisoesBlocos(blocos)
        return self.confereColisoesParede(largura, altura)

    def confereColisoesParede(self, largura, altura):
        if self.shape.x <= self.tamanho:
            self.vel[0] = self.velX
        elif self.shape.x >= largura - self.tamanho:
            self.vel[0] = -self.velX

        if self.shape.y <= self.tamanho:
            self.vel[1] = self.velY
        if self.shape.y >= altura - self.tamanho:
            return False
        return True

    def confereColisaoJogador(self, jogador):
        if jogador.collidepoint(self.shape.x, self.shape.y):
            self.contador += 1

            if self.contador == 3 and self.velY < 50:
                self.contador = 0
                self.velY += 1
                self.velX += 1

            if self.vel[0] > 0:
                self.vel[0] =  self.velX

            elif self.vel[0] < 0:
                self.vel[0] = - self.velX
            self.vel[1] = - self.velY

    def confereColisoesBlocos(self, blocos):
        somColisao = pg.mixer.Sound("smw_coin.wav")
        for bloco in blocos.blocos:
            if self.shape.colliderect(bloco.shape):
                blocos.blocos.remove(bloco)
                somColisao.play()
                pts.somarPontos()
                if self.vel[1] < 0:
                    self.vel[1] = self.velY
                elif self.vel[1] > 0:
                    self.vel[1] = -self.velY
            