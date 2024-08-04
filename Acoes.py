from abc import ABC, abstractmethod
from random import randint

import pokemon
from Jogador import Jogador

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


class Round_random(Combate):
    def __init__(self, jogador, rival):
        self.jogador = jogador
        self.rival = rival
        
    def perdeu_XP(self):
        '''
        Simula a perda de HP do Pokémon do jogador após receber dano do rival.
        '''
        pokemon_atual= self.jogador.get_pokemon_atual()
        if  pokemon_atual is None:
            print('\t\n Nenhum pokemon para receber dano!\t\n==================================================')
            return False

        dano = self.rival['Dano'] * randint(1,3)
        pokemon_atual['Hp'] -= dano
        print(f"\t\n Você recebeu {dano} de dano do {self.rival['Nome']}!")
        
        if pokemon_atual['Hp'] <= 0:
            print(f"\t\n Seu {pokemon_atual['Nome']} foi derrotado")
            return True
        return False
    
    def atacou(self):
        '''
        Simula o ataque do Pokémon do jogador ao rival.
        '''
        pokemon_atual= self.jogador.get_pokemon_atual()
        if pokemon_atual is None:
            print('\t\n Nenhum Pokémon para atacar!\t\n==================================================')
            return False
        
        dano =pokemon_atual['Dano'] * randint(1,3)
        self.rival['Hp'] -= dano
        print(f"\t\n Sua jogada-{pokemon_atual['Nome']} causou {dano} de dano em {self.rival['Nome']}!")
        
        if self.rival['Hp'] <=0:
            print(f"\t\n {self.rival['Nome']} foi derrotado!")
            return True
        return False
        

    def ganhou(self):
        '''
        Atualiza o estado do Pokémon do jogador após ganhar a batalha.
        '''
        pokemon_atual= self.jogador.get_pokemon_atual()
        if pokemon_atual:
            bonus_dano = randint(3,7)
            pokemon_atual['Dano'] += bonus_dano
            self.jogador.set_nivel(self.jogador.get_nivel() + 1)  # Atualiza o nível usando o método setter
            pokemon_atual['Hp'] = min(300 + (20 * self.jogador.get_nivel()), 600)
            print("\t\n==================================================")
            print(f"\t\nVocê ganhou a batalha! Ganhou {bonus_dano} de Dano.")
            print(f"\t\nNovo Nível do Jogador: {self.jogador.get_nivel()}\t\nA vida do seu Pokémon: {pokemon_atual['Hp']} \t\nO dano Mínimo: {pokemon_atual['Dano']} ")
            print(f"\t\nSua patente atual é: {self.jogador._Jogador__patente}")
            print("\t\n==================================================")
            
            return
        

    def perdeu(self):
        '''
        Informa que o Pokémon do jogador foi derrotado e que o jogo terminou
        '''
        pokemon.listar_pokemon()
        print(f"\t\n Fim de jogo \t\n==================================================")
        pokemon.limpar_lista()
        
        return
       

         
class Round_Combate(Combate):
    def __init__(self, jogador, rival):
        self.jogador = jogador
        self.rival = rival
        
    
    def perdeu_XP(self):
        '''
        Simula a perda de HP do Pokémon do jogador após receber dano do rival.
        '''
        pokemon_atual= self.jogador.get_pokemon_atual()
        if  pokemon_atual is None:
            print('\t\n Nenhum pokemon para receber dano!\t\n==================================================')
            return False

        dano = self.rival['Dano'] * randint(1,3)
        pokemon_atual['Hp'] -= dano
        print(f"\t\n  Você recebeu {dano} de dano do {self.rival['Nome']}!")
        if pokemon_atual['Hp'] <= 0:
            print(f"\t\n Seu {pokemon_atual['Nome']} foi derrotado")
            return True
        return False
    
    def atacou(self):
        '''
        Simula o ataque do Pokémon do jogador ao rival.
        '''
        pokemon_atual= self.jogador.get_pokemon_atual()
        if pokemon_atual is None:
            print('\t\n Nenhum Pokémon para atacar!\t\n==================================================')
            return False
        
        dano = pokemon_atual['Dano'] * 3
        self.rival['Hp'] -= dano
        print(f"\t\n Sua jogada-{pokemon_atual['Nome']} causou {dano} de dano em {self.rival['Nome']}!")
        
        if self.rival['Hp'] <=0:
            print(f"\t\n {self.rival['Nome']} foi derrotado!")
            return True
        return False
    
    def trocar_pokemom(self): 
        """
        Permite o jogador trocar o pokemons paraa proxima batalha 
        
        """
        self.jogador.Listar_pokemon_usuario() 
        while True:
            try:
                escolhido= input("Escolha o ID do pokémon que você deseja usar: ").strip()
                if not escolhido.isdigit():
                    raise ValueError(" ID deve ser um número")
                
                escolhido = int(escolhido)
                novo_pokemon = next((p for p in pokemon.Lista_pokemon if p["ID"] == escolhido), None)
                if novo_pokemon: 
                    self.jogador.set_pokemon_atual(novo_pokemon)
                    print(f'\t\n==================================================\n Você escolheu: {self.jogador.get_pokemon_atual()["Nome"]}')
                    break
                else: 
                    print(" Id inválido, digite novamente")
            except ValueError as e:
                print(f"Entrada invalida {e} !!!")
            except StopIteration:
                print("ID inválido, digite novamente ")
        return
        
    
    def ganhou(self):
        '''
        Atualiza o estado do Pokémon do jogador após ganhar a batalha.
        '''
        pokemon_atual = self.jogador.get_pokemon_atual()
        
        if pokemon_atual:
            pokemon_atual['Dano'] += 5
            novo_nivel = self.jogador.get_nivel() + 1
            self.jogador.set_nivel(novo_nivel)
            pokemon_atual['Hp'] = min(300 + (20 *novo_nivel), 800)
            print("\t\n==================================================")
            print("\t\n Você ganhou a batalha! Ganhou +20 hP e +5 de Dano.")
            print(f"\t\n Novo Nível do Jogador: {self.jogador.get_nivel()}\t\n A vida do seu pokémon : {pokemon_atual['Hp']} \t\n O dano Minimo : {pokemon_atual['Dano']} ")
            print(f"\t\nSua patente atual é: {self.jogador._Jogador__patente}")
            print("\t\n==================================================")
            trocar = input("\t\n Você deseja trocar de Pokémon: (s/n)").strip().lower()
            if trocar == 's':
                self.trocar_pokemom()
                if self.jogador.get_pokemon_atual():
                    print(f"\t\n Pokémon atual após troca: {self.jogador.get_pokemon_atual()['Nome']}")
            return
        

    def perdeu(self):
        '''
        Informa que o Pokémon do jogador foi derrotado e que o jogo terminou
        '''
        pokemon.listar_pokemon()
        print(f"\t\n Fim de jogo \t\n==================================================")
        pokemon.limpar_lista()
        return
       

         