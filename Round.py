from abc import ABC, abstractmethod
from random import randint
import pokemon
class Combate(ABC):
    @abstractmethod
    def Perdeu_XP(self, rival):
        '''
        Dano do pokemon é um numero random de 1 a 10 x a sua força 
        Quando o jogador receber o dano do pokemon ele irar ter
        uma perde de xp equivaente a o dano do oponente 
        '''
        pass

    @abstractmethod
    def Atacou(self):
        '''
        Dano do jogador é um numero random de 1 a 10 x a sua força 
        
        Quando o jogador atacar aqui o pokemon
        perde xp equivalente a o dano do jogador 
        '''
        pass

    @abstractmethod
    def Ganhou(self):
        '''
        No Final da partida o jogador tem sua bonificação 
        caso tenha ganhado ele sobe 1 nivel e ganha + 20 xp e 5 de força 

        '''
        pass
    
    @abstractmethod
    def Perdeu(self):
        '''
        No final o jogdor perdeu a partida então 
        ele só recupera sua vida e mantem a força que ja tinha não sobe de level
        '''
        pass


class Round(Combate):
    def __init__(self):
        self.rival = pokemon.Oponente()
        
    def Perdeu_XP(self, rival):
        print(" antes do dano ",rival)
        dano = rival['Dano'] * randint(1,3)
        rival["Hp"] -=dano
        print( "depois do dano ",rival)
        print(pokemon.lista_pokemons_emfrentados)
        # Dano do pokemon é um número random de 1 a 10 x a sua força
        # Quando o jogador receber o dano do pokemon ele irá ter
        # uma perda de xp equivalente ao dano do oponente
      

    def Atacou(self):
            # Dano do jogador é um número random de 1 a 10 x a sua força
            # Quando o jogador atacar o pokemon
            # perde xp equivalente ao dano do jogador
        pass

    def Ganhou(self):
            # No final da partida, se o jogador ganhar,
            # ele sobe 1 nível e ganha +20 xp e 5 de força
        pass

    def Perdeu(self):
            # No final, se o jogador perder a partida,
            # ele só recupera sua vida e mantém a força que já tinha, não sobe de nível
        pass
