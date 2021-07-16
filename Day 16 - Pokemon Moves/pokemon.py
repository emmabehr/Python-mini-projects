import requests 

def get_pokemon(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    response = requests.get(url)

    pokemon = response.json()
    return pokemon

def save_pokemon(pokemon):
    pokemon_data = ""
    with open("pokemon.txt", "r+") as pokemon_file:
        pokemon_data = pokemon_file.read()

    pokemon_data = f"{pokemon_data}{pokemon['name']}\n\n"
    for move in pokemon["moves"]:
        pokemon_data = f"{pokemon_data}{move['move']['name']}\n"

    pokemon_data = f"{pokemon_data}\n"

    with open("pokemon.txt", "w+") as pokemon_file:
        pokemon_file.write(pokemon_data)

pokemon_list = []
add_pokemon = True

while add_pokemon:
    pokemon_number = input("What is the ID of the pokemon you want to search? ")
    pokemon_list.append(int(pokemon_number))
    continue_add = input("Continue adding pokemon? (y/n) ")
    if continue_add.lower() != "y":
        add_pokemon = False

for pokemon_id in pokemon_list:
    pokemon = get_pokemon(pokemon_id)
    save_pokemon(pokemon)