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

def test_as_vale_onze():
    jogo = Blackjack()
            
    jogo.adicionar_carta(1, "A")
    jogo.adicionar_carta(1, "9")

    pontos = jogo.calcular_pontuacao(1)
        
    assert pontos == 20

def test_as_vale_um():
    jogo = Blackjack()
                
    jogo.adicionar_carta(1, "A")
    jogo.adicionar_carta(1, "9")
    jogo.adicionar_carta(1, "5")
    
    pontos = jogo.calcular_pontuacao(1)
            
    assert pontos == 15


def test_jogador_estorou():
    jogo = Blackjack()

    jogo.adicionar_carta(1, "10")
    jogo.adicionar_carta(1, "8")
    jogo.adicionar_carta(1, "5")
        
    
    assert jogo.estorou(1) is True

def test_jogador_nao_estorou():
    jogo = Blackjack()
    
    jogo.adicionar_carta(1, "10")
    jogo.adicionar_carta(1, "8")            
        
    assert jogo.estorou(1) is False


def test_adicionar_carta_jogador2():
    jogo = Blackjack()
        
    jogo.adicionar_carta(2, "7")
            
    assert jogo.mao_jogador2 == ["7"]





