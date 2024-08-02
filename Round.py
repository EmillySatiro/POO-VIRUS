from abc import ABC, abstractmethod
from random import randint
import pokemon


class Combate(ABC):
    @abstractmethod
    def perdeu_XP(self, rival):
        '''
        Dano do pokemon é um numero random de 1 a 10 x a sua força 
        Quando o jogador receber o dano do pokemon ele irar ter
        uma perde de xp equivaente a o dano do oponente 
        '''
        pass
    
    @abstractmethod
    def atacou(self):
        '''
        Quando jogador ataca, o pokémon rival perde hp equivalente ao dano do jogador 
        '''
        pass


    @abstractmethod
    def ganhou(self):
        '''
        No Final da partida o jogador tem sua bonificação 
        caso tenha ganhado ele sobe 1 nivel e ganha + 20 xp e 5 de força 

        '''
        pass
    
    @abstractmethod
    def perdeu(self):
        '''
        fim de jogo 
        '''
        pass


class Round(Combate):
    def __init__(self, jogador, rival):
        self.jogador = jogador
        self.rival = rival
        
    def perdeu_XP(self):
        if not self.jogador.pokemon_atual:
            print('Nenhum pokemon para receber dano!')
            return False
        
        dano = self.rival['Dano'] * randint(1,3)
        self.jogador.pokemon_atual['Hp'] -= dano
        print(f"Você recebeu {dano} de dano do {self.rival['Nome']}!")
        if self.jogador.pokemon_atual['Hp'] <= 0:
            print(f"{self.jogador.pokemon_atual['Nome']} foi derrotado")
            return True
        return False
    
    def atacou(self):
        if not self.jogador.pokemon_atual:
            print('Nenhum Pokémon para atacar!')
            return False
        
        dano = self.jogador.pokemon_atual['Dano'] * randint(1,3)
        self.rival['Hp'] -= dano
        print(f" {self.jogador.pokemon_atual['Nome']} causou {dano} de dano em {self.rival['Nome']}!")
        
        if self.rival['Hp'] <=0:
            print(f"{self.rival['Nome']} foi derrotado!")
            return True
        return False
        

    def ganhou(self):
        if hasattr(self.jogador, 'pokemon_atual'):
            self.jogador.pokemon_atual['Hp'] = 100 
            self.jogador.pokemon_atual['Dano'] = self.jogador.pokemon_atual.get('Dano', 0) + 5
            print("Você ganhou a batalha! Ganhou +20 hP e +5 de Dano.")
        

    def perdeu(self):
        print(f"Fim de jogo")
       
            
    
