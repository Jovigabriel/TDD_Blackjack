class Blackjack:

    def __init__(self):
        self.mao_jogador1 = []

    def adicionar_carta(self, jogador, valor):

        if jogador == 1:
            self.mao_jogador1.append(valor)