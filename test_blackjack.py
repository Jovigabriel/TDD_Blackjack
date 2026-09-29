from blackjack import Blackjack
#from blackjack_ref import Blackjack



def test_criar_jogo():
    jogo = Blackjack()

    assert jogo is not None

    
def test_adicionar_carta():
    jogo = Blackjack()

    jogo.adicionar_carta(1, "5")
    
    assert jogo.maos[1] == ["5"] #verificando se a mao do jogador 1 só tem 5

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

    assert jogo.maos[2] == ["7"]


def test_jogador1_vence_com_maior_pontuacao():
    jogo = Blackjack()

    jogo.adicionar_carta(1, "10")
    jogo.adicionar_carta(1, "9")

    jogo.adicionar_carta(2, "10")
    jogo.adicionar_carta(2, "7")

    assert jogo.determinar_vencedor() == 1

def test_jogador_que_estoura_perde():
    jogo = Blackjack()

    jogo.adicionar_carta(1, "10")
    jogo.adicionar_carta(1, "10")
    jogo.adicionar_carta(1, "5")

    jogo.adicionar_carta(2, "10")
    jogo.adicionar_carta(2, "5")

    assert jogo.determinar_vencedor() == 2


def test_empate():
    jogo = Blackjack()

    jogo.adicionar_carta(1, "10")
    jogo.adicionar_carta(1, "8")

    jogo.adicionar_carta(2, "K")
    jogo.adicionar_carta(2, "8")

    assert jogo.determinar_vencedor() == "empate"


def test_criar_baralho():
    jogo = Blackjack()

    jogo.criar_baralho()

    assert len(jogo.baralho) == 52


def test_distribuir_cartas_iniciais():
    jogo = Blackjack()

    jogo.criar_baralho()
    jogo.distribuir_cartas()

    assert len(jogo.maos[1]) == 2
    assert len(jogo.maos[2]) == 2

def test_comprar_carta():
    jogo = Blackjack()

    jogo.criar_baralho()
    jogo.comprar_carta(1)

    assert len(jogo.maos[1]) == 1


def test_visualizar_mesa():
    jogo = Blackjack()

    jogo.adicionar_carta(1, "10")
    jogo.adicionar_carta(2, "7")

    mesa = jogo.visualizar_mesa()

    assert mesa[1] == ["10"]
    assert mesa[2] == ["7"]