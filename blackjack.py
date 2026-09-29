class Blackjack:

    def __init__(self):
        self.mao_jogador1 = []

    def adicionar_carta(self, jogador, valor):

        if jogador == 1:
            self.mao_jogador1.append(valor)

    def calcular_pontuacao(self, jogador):
        somatorio = 0
        
        for ponto in self.mao_jogador1:
            ponto_int = int(ponto)
            somatorio = somatorio + ponto_int

        return somatorio