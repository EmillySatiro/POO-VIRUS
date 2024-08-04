import pokemon

class Jogador: 
    def __init__(self, nome):
        self.__nome = nome
        self.__nivel = 0
        self.__pokemon_atual = None
        self.__pokemon_list = [] 
        self.__patente = 'Novato'

    #metodos para acessar atributos privados, se necessario 
    def get_nome(self):
        return self.__nome
    
    def get_nivel(self):
        return self.__nivel
    
    
    def get_pokemon_atual(self):
        return self.__pokemon_atual
    
    def get_pokemon_list(self):
        return self.__pokemon_list
    
    def get_patente(self):
        return self.__patente
    
    def set_nome(self,nome):
        self.__nome = nome 
    
    def set_nivel(self, nivel):
        self.__nivel = nivel 
        self.confere_patente()
    
    def set_pokemon_atual(self,pokemon):
        self.__pokemon_atual = pokemon
        
    def set_pokemon_list(self, pokemon_list):
        self.__pokemon_list = pokemon_list
        
    def set_pokemon_patente(self, patente):
        self.__patente = patente 
    
        
    def Listar_pokemon_usuario(self):
        ''' Exibe a Lista de pokémon para o jogador '''
        print(f"\nNome do Jogador: {self.__nome}\nNível do Jogador: {self.__nivel}\n")
        # usuario vai selecionar o pokemon que irar jogar 
        print(" Pokémons disponivéis: ")
        for p in pokemon.Lista_pokemon:
            pokemon.imprimir_cartas(p)
      
    def escolher_pokemon(self):
        ''' Permite ao jogador escolher um pokémon a partir de uma lista'''
        self.Listar_pokemon_usuario()
        while True:
            try:
                escolhido= input("Escolha o ID do pokémon que você deseja usar: ").strip()
                if not escolhido.isdigit():
                    raise ValueError(" ID deve ser um número")
                
                escolhido = int(escolhido)
                self.__pokemon_atual = next(p for p in pokemon.Lista_pokemon if p["ID"] == escolhido)
                print(f'\t\n==================================================\n Você escolheu: {self.__pokemon_atual["Nome"]}')
                break
            except ValueError as e:
                print(f"Entrada invalida {e} !!!")
            except StopIteration:
                print("ID invalido, digite novamente ")
        return
 
    def confere_patente(self):
        ''' Confere a patente e atualiza '''
        if self.__nivel >= 30:
            nova_patente =  " Treinador Supremo"
        elif self.__nivel>= 25:
            nova_patente =  " Treinador de Lendas"
        elif self.__nivel>= 20:
            nova_patente =  " Treinador de Elite "
        elif self.__nivel>= 15:
            nova_patente =  " Treinador de Monstrons"
        elif self.__nivel>= 10:
            nova_patente =  " Treinador Experiente"
        elif self.__nivel>= 5:
            nova_patente =  " Treinador Interediario"
        else: 
            nova_patente = "Novato"
        
        if self.__patente != nova_patente:
            self.__patente = nova_patente
            
            print(f"\t\n Você atigingiu a patente de: {self.__patente}")
            
            
     