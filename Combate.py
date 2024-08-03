import pokemon
import Acoes   
import Jogador  
import artesac
     
class Jogo_random:
    def __init__(self):
        nome = input(" Digite seu nome: ").strip()
        self.jogador = Jogador.Jogador(nome)
    
    def iniciar(self):
        self.jogador.escolher_pokemon()
        while True:
            rival = pokemon.Oponente()
            if not rival:
                print("Não há mais oponentes disponíveis!")
                break
            
            input(f"\t\n Pressione Enter para continuar...\n ==================================================")
            
            combate = Acoes.Round_random(self.jogador, rival)
            
            while True:
                if combate.perdeu_XP():# pokemon do usuario morreu durante o combate 
                    combate.perdeu()
                    return

                if combate.atacou():
                    combate.ganhou()
                    break
                
                if self.jogador.pokemon_atual['Hp'] <= 0:# pokemon do usuario morreu ao final do combate 
                    combate.perdeu()
                    return
class Jogo_batalha:
    def __init__(self):
        nome = input(" Digite seu nome: ").strip()
        self.jogador = Jogador.Jogador(nome)
    
    def iniciar(self):
        self.jogador.escolher_pokemon()
        while True:
            rival = pokemon.Oponente()
            if not rival:
                print("Não há mais oponentes disponíveis!")
                break
            
            input(f"\t\n Você está enfrentando: {rival['Nome']}. Pressione Enter para continuar...\n ==================================================")
            
            combate = Acoes.Round_Combate(self.jogador, rival)
            
            while True:
                if combate.perdeu_XP():# pokemon do usuario morreu durante o combate 
                    combate.perdeu()
                    return

                if combate.atacou():
                    combate.ganhou()
                    break
                
                if self.jogador.pokemon_atual['Hp'] <= 0:# pokemon do usuario morreu ao final do combate 
                    combate.perdeu()
                    return
                
def menu():
    while True:
        print("\n========================================")
        print("                 MODOS DE JOGO")
        print("\n========================================")
        print("1. Jogar no modo Aleatório")
        print("2. Jogar no modo Batalha")
        print("3. sair")
        print("\n========================================")
        
        escolha = input("Escolha uma opção (1/2/3): ").strip()
        
        if escolha =='1':
            jogo = Jogo_random()
            jogo.iniciar()
        elif escolha =='2':
            Jogo_batalha()
            jogo.iniciar()
        elif escolha == '3':
            print("SAINDO DO JOGO .....")
            break
        else:
            print("Opção inválida, tente novamente!")
            
def Informacoes():
    print("\n========================================")
    print("            Instruções Do jogo")
    print("1. Jogar no modo Aleatório: ")
    print("   Neste modo, você enfrentará oponentes aleatórios em uma sequência de batalhas.")
    print("   Cada vez que vencer um oponente, você ganhará pontos de experiência (XP) que são convertidos em dano e HP para o seu Pokémon.")
    print("   O objetivo é derrotar o máximo de oponentes possível e acumular a maior quantidade de XP.")
    print("   Se o seu Pokémon perder toda a sua HP durante uma batalha, você perderá o jogo.")
    print("\n2. Jogar no modo Batalha: ")
    print("   - Neste modo, você enfrentará oponentes em batalhas mais estruturadas.")
    print("   - Você pode trocar seu Pokémon durante a batalha se desejar.")
    print("   - O objetivo é derrotar o oponente e, se vencer, você pode trocar seu Pokémon.")
    print("   Cada vez que vencer um oponente, você ganhará pontos de experiência (XP) que são convertidos em dano e HP para o seu Pokémon.")
    print("\nPressione Enter para voltar ao menu principal.")
    input()

inicio = artesac.tela_test()