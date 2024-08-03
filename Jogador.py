import pokemon

class Jogador: 
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 0
        self.pokemon_atual = None
        
        
    def Listar_pokemon_usuario(self):

        print(f"\nNome do Jogador: {self.nome}\nNível do Jogador: {self.nivel}\n")
        # usuario vai selecionar o pokemon que irar jogar 
        print(" Pokémons disponivéis: ")
        for p in pokemon.Lista_pokemon:
            pokemon.imprimir_cartas(p)
      
    def escolher_pokemon(self):
        self.Listar_pokemon_usuario()
        while True:
            try:
                escolhido= input("Escolha o ID do pokémon que você deseja usar: ").strip()
                if not escolhido.isdigit():
                    raise ValueError(" ID deve ser um número")
                
                escolhido = int(escolhido)
                self.pokemon_atual = next(p for p in pokemon.Lista_pokemon if p["ID"] == escolhido)
                print(f'\t\n==================================================\n Você escolheu: {self.pokemon_atual["Nome"]}')
                break
            except ValueError as e:
                print(f"Entrada invalida {e} !!!")
            except StopIteration:
                print("ID invalido, digite novamente ")
        return
 