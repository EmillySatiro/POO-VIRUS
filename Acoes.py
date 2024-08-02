from abc import ABC, abstractmethod
from random import randint

import pokemon

class Combate(ABC):
    @abstractmethod
    def perdeu_XP(self, rival):
        ''' 
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
        '''
        Simula a perda de HP do Pokémon do jogador após receber dano do rival.
        '''
        if not self.jogador.pokemon_atual:
            print('\t\n Nenhum pokemon para receber dano!\t\n==================================================')
            return False
        
        dano = self.rival['Dano'] * randint(1,3)
        self.jogador.pokemon_atual['Hp'] -= dano
        print(f"\t\n Você recebeu {dano} de dano do {self.rival['Nome']}!")
        if self.jogador.pokemon_atual['Hp'] <= 0:
            print(f"\t\n Seu {self.jogador.pokemon_atual['Nome']} foi derrotado")
            return True
        return False
    
    def atacou(self):
        '''
        Simula o ataque do Pokémon do jogador ao rival.
        '''
        if not self.jogador.pokemon_atual:
            print('\t\n Nenhum Pokémon para atacar!\t\n==================================================')
            return False
        
        dano = self.jogador.pokemon_atual['Dano'] * randint(1,3)
        self.rival['Hp'] -= dano
        print(f"\t\n Sua jogada-{self.jogador.pokemon_atual['Nome']} causou {dano} de dano em {self.rival['Nome']}!")
        
        if self.rival['Hp'] <=0:
            print(f"\t\n {self.rival['Nome']} foi derrotado!")
            return True
        return False
        

    def ganhou(self):
        '''
        Atualiza o estado do Pokémon do jogador após ganhar a batalha.
        '''
        if hasattr(self.jogador, 'pokemon_atual'):
            self.jogador.pokemon_atual['Hp'] = 100 
            self.jogador.pokemon_atual['Dano'] = self.jogador.pokemon_atual.get('Dano', 0) + 5
            self.jogador.nivel +=1
            print("\t\n Você ganhou a batalha! Ganhou +20 hP e +5 de Dano.")
            print(f"\t\n Novo Nível do Jogador: {self.jogador.nivel}\t\n==================================================")
        

    def perdeu(self):
        '''
        Informa que o Pokémon do jogador foi derrotado e que o jogo terminou
        '''
        pokemon.listar_pokemon()
        print(f"\t\n Fim de jogo \t\n==================================================")
       
            
    
