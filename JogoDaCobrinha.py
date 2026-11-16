import pygame as pg
import random

pg.init()

velocidade = 5
largura, altura = 900, 700
tela = pg.display.set_mode((largura, altura))

clock = pg.time.Clock()

tamPadrao = 30
tamMaca = 30
tamLimiteCobra = 15

def novaCor():
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    conjCores = (color1, color2, color3)
    return conjCores

corTela = (0, 0, 25)
corCobra = novaCor()
corMaca = novaCor()


cobraPos = pg.Vector2(tela.get_width()/2, tela.get_height()/2)
macaPos = pg.Vector2( random.randint(tamMaca, largura-tamMaca), random.randint(tamMaca, altura-tamMaca))
controlPos = pg.Vector2(velocidade, 0)

listaCobra = []

while True:
    tela.fill(corTela)

    key = pg.key.get_pressed()
    if key[pg.K_w]:
        controlPos.y = velocidade * -1
        controlPos.x = 0
    elif key[pg.K_s]:
        controlPos.y = velocidade
        controlPos.x = 0
    elif key[pg.K_d]:
        controlPos.y = 0
        controlPos.x = velocidade
    elif key[pg.K_a]:
        controlPos.y = 0
        controlPos.x = velocidade * -1

    cobraPos.x += controlPos.x
    cobraPos.y += controlPos.y

    cobra = pg.draw.rect(tela, corCobra, (cobraPos.x, cobraPos.y, tamPadrao, tamPadrao), border_radius=20)
    maca = pg.draw.rect(tela, corMaca, (macaPos.x, macaPos.y, tamMaca, tamMaca), border_radius=20)

    listaCabeca = []
    listaCabeca.append(cobraPos.x)
    listaCabeca.append(cobraPos.y)
    listaCobra.append(listaCabeca)

    for pos in listaCobra:
        pg.draw.rect(tela, corCobra,(pos[0], pos[1], tamPadrao, tamPadrao))

    if len(listaCobra) > tamLimiteCobra:
        del listaCobra[0]

    if maca.colliderect(cobra):
        corMaca = novaCor()
        tamLimiteCobra += 15
        macaPos.x = random.randint(tamMaca, largura-tamMaca)
        macaPos.y = random.randint(tamMaca, altura-tamMaca)

    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    pg.display.update()
