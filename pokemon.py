from random import randint

Lista_pokemon = [
    {"ID": 1,"Nome": " Bulbasaur", "Tipo": "Planta, poison", "Hp":100,"Dano":15 },
    {"ID": 3,"Nome": " Ivysaur", "Tipo": "Planta, poison","Hp":100,"Dano":25 },
    {"ID": 4,"Nome": " Venusaur", "Tipo": "Planta, poison","Hp":100,"Dano":35},
    {"ID": 5,"Nome": " Charmander", "Tipo": "Fogo","Hp":100,"Dano":20},
    {"ID": 6,"Nome": " Charmeleon", "Tipo": "Fogo","Hp":100,"Dano":30},
    {"ID": 7,"Nome": " Charizard", "Tipo": "fogo, Flying","Hp":100, "Dano": 45},
    {"ID": 8,"Nome": " Squirtle", "Tipo": "Água","Hp":100,"Dano":18},
    {"ID": 9,"Nome": " Wartortle", "Tipo": "Água","Hp":100,"Dano":28},
    {"ID": 10,"Nome": " Blastoise", "Tipo": "Água","Hp":100,"Dano":40},
    {"ID": 11,"Nome": " Caterpie", "Tipo": "Bug","Hp":100,"Dano":10},
    {"ID": 12,"Nome": " Metapod", "Tipo": "Bug","Hp":100,"Dano":15},
    {"ID": 13,"Nome": " Butterfree", "Tipo": "Bug , Flying","Hp":100,"Dano":30},
    {"ID": 14,"Nome": " Beedrill", "Tipo": "Bug, Poison","Hp":100,"Dano":35},
    {"ID": 15,"Nome": " Pidgey", "Tipo": "Normal, Flying","Hp":100,"Dano":20},
    {"ID": 16,"Nome": " Arbok", "Tipo": "Poison","Hp":100,"Dano":30},
    {"ID": 17,"Nome": " Pikachu", "Tipo": "Electric","Hp":100,"Dano":25},
    {"ID": 18,"Nome": " Sandslash", "Tipo": "Ground","Hp":100,"Dano":30},
    {"ID": 19,"Nome": " Nidoking", "Tipo": "Poison, Ground","Hp":100,"Dano":40},
    {"ID": 20,"Nome": " Wigglytuff", "Tipo": "Normal, Fada","Hp":100,"Dano":25},
    {"ID": 21,"Nome": " Zubat", "Tipo": "Poison, Flying","Hp":100,"Dano":20},
    {"ID": 22,"Nome": " Meowth", "Tipo": "Normal","Hp":100,"Dano":22},
    {"ID": 23,"Nome": " Psyduck", "Tipo": "Água","Hp":100,"Dano":20},
    {"ID": 24,"Nome": " Gengar", "Tipo": "Ghost, poison","Hp":100,"Dano":35},
    {"ID": 25,"Nome": " Onix", "Tipo": "Rock, Ground","Hp":100,"Dano":25},
    {"ID": 26,"Nome": " Snorlax", "Tipo": "Normal","Hp":100,"Dano":30 },
    {"ID": 27,"Nome": " Mewtwo", "Tipo": "Psíquico","Hp":100,"Dano":50},
    {"ID": 28,"Nome": " Noctowl", "Tipo": "Normal, Flying","Hp":100,"Dano":28 },
    {"ID": 29,"Nome": " Espeon", "Tipo": "Psíquico","Hp":100,"Dano":35},
    {"ID": 30,"Nome": " Sneasel", "Tipo": "Ice","Hp":100,"Dano":30},
]

lista_pokemons_emfrentados = []
# Função para escolher o pokemon para o combate 

def Oponente():
    sorteado = randint(1,30)
    oponente = next((p for p in Lista_pokemon if p["ID"] == sorteado), None)
    if oponente:
        lista_pokemons_emfrentados.append(oponente)
    return oponente

def listar_pokemon():
    for x in lista_pokemons_emfrentados:
        print(
            f"\t\n=========================\n Nome: {x['Nome']}\t\n Tipo: {x['Tipo']}\t\n HP:{x['Hp']}\t\n Dano minimo: {x['Dano']}\t\n=========================\n"
        )
    
    

listar_pokemon()