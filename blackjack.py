class Blackjack:

    def __init__(self):
        self.maos = {
            1: [],
            2: []
        }

    def adicionar_carta(self, jogador, valor):
        self.maos[jogador].append(valor)

    def calcular_pontuacao(self, jogador):
        total = 0
        quantidade_as = 0

        for carta in self.maos[jogador]:
            total += self.valor_carta(carta)

            if carta.upper() == "A":
                quantidade_as += 1

        while total > 21 and quantidade_as > 0:
            total -= 10
            quantidade_as -= 1

        return total

    def valor_carta(self, carta):
        carta = carta.upper()

        if carta == "A":
            return 11

        if carta in ["J", "Q", "K"]:
            return 10

        return int(carta)

    def estorou(self, jogador):
        return self.calcular_pontuacao(jogador) > 21

    
    

       