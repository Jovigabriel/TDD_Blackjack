class Blackjack:

    def __init__(self):
        self.maos = {
            1: [],
            2: []
        }
        self.baralho = []

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

    def determinar_vencedor(self):
        pontos1 = self.calcular_pontuacao(1)
        pontos2 = self.calcular_pontuacao(2)

        if pontos1 > pontos2:
            return 1

        return 2

    
    def determinar_vencedor(self):
        pontos1 = self.calcular_pontuacao(1)
        pontos2 = self.calcular_pontuacao(2)

        if pontos1 > 21 and pontos2 > 21:
            return "empate"

        if pontos1 > 21:
            return 2

        if pontos2 > 21:
            return 1

        if pontos1 == pontos2:
            return "empate"

        if pontos1 > pontos2:
            return 1

        return 2

    def criar_baralho(self):
        valores = [
            "A", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K"
        ]

        self.baralho = valores * 4

    def distribuir_cartas(self):
        self.maos[1].append(self.baralho.pop())
        self.maos[2].append(self.baralho.pop())

        self.maos[1].append(self.baralho.pop())
        self.maos[2].append(self.baralho.pop())