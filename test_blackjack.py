from blackjack import Blackjack
#from blackjack_ref import Blackjack



def test_criar_jogo():
    jogo = Blackjack()

    assert jogo is not None

    
def test_adicionar_carta():
    jogo = Blackjack()

    jogo.adicionar_carta(1, "5")
    
    assert jogo.mao_jogador1 == ["5"] #verificando se a mao do jogador 1 só tem 5

def test_calcular_pontuacao():
    jogo = Blackjack()
    
    jogo.adicionar_carta(1, "5")
    jogo.adicionar_carta(1, "7")
    pontos = jogo.calcular_pontuacao(1)

    assert pontos == 12

def test_calcular_pontuacoes_letras():
    jogo = Blackjack()
        
    jogo.adicionar_carta(1, "J")
    jogo.adicionar_carta(1, "K")
    pontos = jogo.calcular_pontuacao(1)
    
    assert pontos == 20

