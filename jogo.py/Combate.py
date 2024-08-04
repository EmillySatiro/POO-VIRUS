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
                if combate.perdeu_XP(): # pokemon do usuario morreu durante o combate 
                    combate.perdeu()
                    return

                if combate.atacou():
                    combate.ganhou()
                    break
                pokemon_atual = self.jogador.get_pokemon_atual()
                if pokemon_atual and pokemon_atual['Hp'] <= 0:# pokemon do usuario morreu ao final do combate 
                    pokemon_atual['Hp'] = 300
                    combate.perdeu()
                    return
class Jogo_batalha:
    def __init__(self):
        nome = input(" Digite seu nome: ").strip()
        self.jogador = Jogador.Jogador(nome)
        
    print("\n========================================")
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
                
                pokemon_atual= self.jogador.get_pokemon_atual()
                if pokemon_atual and pokemon_atual['Hp'] <= 0:# pokemon do usuario morreu ao final do combate 
                    pokemon_atual['Hp'] = 300
                    combate.perdeu()
                    return
    print("\n========================================")
                
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
            jogo = Jogo_batalha()
            jogo.iniciar()
        elif escolha == '3':
            artesac.tela_fim()
            #print de nome, nivel, patente 
            break
        else:
            print("Opção inválida, tente novamente!")
            
def Informacoes():
    print("\n========================================================================================================")
    print("                                         Instruções Do jogo")
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
    print("\nPressione Enter para ir ao menu principal.")
    input()

artesac.tela_inicio()
input()
Informacoes()
menu()
