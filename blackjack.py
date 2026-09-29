class Blackjack:

    def __init__(self):
        self.mao_jogador1 = []
        self.mao_jogador2 = []

    def adicionar_carta(self, jogador, valor):

        if jogador == 1:
            self.mao_jogador1.append(valor)

        if jogador == 2:
            self.mao_jogador2.append(valor)
   

    def calcular_pontuacao(self, jogador):

        if jogador == 1:
            mao = self.mao_jogador1
        else:
            mao = self.mao_jogador2

        total = 0
        quantidade_as = 0
            
        for carta in mao:
            total += self.valor_carta(carta)

            if carta.upper() == "A":
                quantidade_as += 1
            
        while total > 21 and quantidade_as > 0:
            total -=10
            quantidade_as -=1
    
        return total

    def valor_carta(self, carta):
        carta = carta.upper()

        if carta == "A":
            return 11

        if carta in ["J", "K", "Q"]:
            return 10

        return int(carta)

    def estorou(self, jogador):
        return self.calcular_pontuacao(jogador) > 21

    
    

       