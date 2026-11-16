import pygame as pg

class Bloco:
    def __init__(self, cor):
        self.cor = cor
        self.shape = None
    def criaBloco(self, posX, posY, largura, altura):
        self.shape = pg.Rect(posX, posY, largura, altura)

class Blocos:
    def __init__(self, cor,):
        self.cor = cor
        self.blocos = []

    def criaBlocos(self, numL, numC, largura, altura):

        self.espacamento = int(largura / (numC * 20.0))
        espacoParaBloco = (largura - self.espacamento * numC)
        blocoLargura = int(espacoParaBloco / numC)
        blocoAltura = (0.3 * altura / numL)

        for i in range(numL):
            for j in range(numC):
                novoBloco = Bloco(self.cor)
                novoBloco.criaBloco(j * (blocoLargura + self.espacamento), i * (blocoAltura + self.espacamento), blocoLargura, blocoAltura)
                self.blocos.append(novoBloco)
