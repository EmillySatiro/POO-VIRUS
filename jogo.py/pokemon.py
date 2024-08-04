from random import randint

Lista_pokemon = [
    {"ID": 1,"Nome": " Lugia", "Tipo": "Psíquico, Flting", "Hp":300,"Dano":35 },
    {"ID": 2,"Nome": " Bulbasaur", "Tipo": "Planta, poison", "Hp":300,"Dano":15 },
    {"ID": 3,"Nome": " Ivysaur", "Tipo": "Planta, poison","Hp":300,"Dano":25 },
    {"ID": 4,"Nome": " Venusaur", "Tipo": "Planta, poison","Hp":300,"Dano":35},
    {"ID": 5,"Nome": " Charmander", "Tipo": "Fogo","Hp":300,"Dano":20},
    {"ID": 6,"Nome": " Charmeleon", "Tipo": "Fogo","Hp":300,"Dano":30},
    {"ID": 7,"Nome": " Charizard", "Tipo": "fogo, Flying","Hp":300, "Dano": 45},
    {"ID": 8,"Nome": " Squirtle", "Tipo": "Água","Hp":300,"Dano":18},
    {"ID": 9,"Nome": " Wartortle", "Tipo": "Água","Hp":300,"Dano":28},
    {"ID": 10,"Nome": " Blastoise", "Tipo": "Água","Hp":300,"Dano":40},
    {"ID": 11,"Nome": " Caterpie", "Tipo": "Bug","Hp":300,"Dano":10},
    {"ID": 12,"Nome": " Metapod", "Tipo": "Bug","Hp":300,"Dano":15},
    {"ID": 13,"Nome": " Butterfree", "Tipo": "Bug , Flying","Hp":300,"Dano":30},
    {"ID": 14,"Nome": " Beedrill", "Tipo": "Bug, Poison","Hp":300,"Dano":35},
    {"ID": 15,"Nome": " Pidgey", "Tipo": "Normal, Flying","Hp":300,"Dano":20},
    {"ID": 16,"Nome": " Arbok", "Tipo": "Poison","Hp":300,"Dano":30},
    {"ID": 17,"Nome": " Pikachu", "Tipo": "Electric","Hp":300,"Dano":25},
    {"ID": 18,"Nome": " Sandslash", "Tipo": "Ground","Hp":300,"Dano":30},
    {"ID": 19,"Nome": " Nidoking", "Tipo": "Poison, Ground","Hp":300,"Dano":40},
    {"ID": 20,"Nome": " Wigglytuff", "Tipo": "Normal, Fada","Hp":300,"Dano":25},
    {"ID": 21,"Nome": " Zubat", "Tipo": "Poison, Flying","Hp":300,"Dano":20},
    {"ID": 22,"Nome": " Meowth", "Tipo": "Normal","Hp":300,"Dano":22},
    {"ID": 23,"Nome": " Psyduck", "Tipo": "Água","Hp":300,"Dano":20},
    {"ID": 24,"Nome": " Gengar", "Tipo": "Ghost, poison","Hp":300,"Dano":35},
    {"ID": 25,"Nome": " Onix", "Tipo": "Rock, Ground","Hp":300,"Dano":25},
    {"ID": 26,"Nome": " Snorlax", "Tipo": "Normal","Hp":300,"Dano":30 },
    {"ID": 27,"Nome": " Mewtwo", "Tipo": "Psíquico","Hp":300,"Dano":45},
    {"ID": 28,"Nome": " Noctowl", "Tipo": "Normal, Flying","Hp":300,"Dano":28 },
    {"ID": 29,"Nome": " Espeon", "Tipo": "Psíquico","Hp":300,"Dano":35},
    {"ID": 30,"Nome": " Sneasel", "Tipo": "Ice","Hp":300,"Dano":30},
]

lista_pokemons_emfrentados = []
# Função para escolher o pokemon para o combate 

def Oponente():
    sorteado = randint(1, len(Lista_pokemon)-1)
    pokemon_escolhido = Lista_pokemon[sorteado]
    print("SEU RIVAL NESSE COMBATE \n")
    imprimir_cartas(pokemon_escolhido)
    lista_pokemons_emfrentados.append(pokemon_escolhido)
    return pokemon_escolhido

def imprimir_cartas(pokemon):
    card_width = 40 
    boder = "="*card_width
    
    def center_text(text,whith):
        return text.center(whith)
    
    print(boder)
    print(center_text("POKÉMON", card_width))
    print(boder)
    print(center_text(f"ID: {pokemon['ID']}", card_width))
    print(center_text(f"Nome: {pokemon['Nome']}", card_width))
    print(center_text(f"Tipo: {pokemon['Tipo']}", card_width))
    print(center_text(f"Hp: {pokemon['Hp']}", card_width))
    print(center_text(f"Dano minimo: {pokemon['Dano']}", card_width))
    print(boder)
    print("\n")
    
def listar_pokemon():
    print("\t\n Lista de pokemons emfrentados: ")
    for x in lista_pokemons_emfrentados:
        imprimir_cartas(x)

def limpar_lista():
    lista_pokemons_emfrentados.clear()
    
    