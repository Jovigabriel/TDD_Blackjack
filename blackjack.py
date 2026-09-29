class Blackjack:

    def __init__(self):
        self.mao_jogador1 = []

    def adicionar_carta(self, jogador, valor):

        if jogador == 1:
            self.mao_jogador1.append(valor)

    def calcular_pontuacao(self, jogador):
        total = 0
            
        for carta in self.mao_jogador1:
            total += self.valor_carta(carta)
    
        return total


    def valor_carta(self, carta):
        carta = carta.upper()

        if carta in ["J", "K", "Q"]:
            return 10

        return int(carta)