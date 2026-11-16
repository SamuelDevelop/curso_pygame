
class Pontos:
    pontos = 0

    @staticmethod
    def somarPontos():
        Pontos.pontos += 1
    
    @staticmethod
    def getPontos():
        return Pontos.pontos