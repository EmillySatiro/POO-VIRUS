import pokemon
import Acoes   
import Jogador  
     
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
            
            input(f"\t\n Você está enfrentando: {rival['Nome']}. Pressione Enter para continuar...\n ==================================================")
            
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
jogo = Jogo_batalha()
jogo.iniciar()