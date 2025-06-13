import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TOKEN'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}


bodyCreatePokemon = {
	"name": "Stas",
	"photo_id": 1002
}

bodyFullUpdatePokemon = {
	"pokemon_id": "335851",
	"name": "Valera",
	"photo_id": 645
}


responseCreatePokemon = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=bodyCreatePokemon)
print(f'{responseCreatePokemon.status_code}: {responseCreatePokemon.text}')


bodyFullUpdatePokemon["pokemon_id"] = responseCreatePokemon.json()["id"] # Для наглядности изменяю имя только что созданному покемону
responseChangeNamePokemon = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=bodyFullUpdatePokemon)
print(f'{responseChangeNamePokemon.status_code}: {responseChangeNamePokemon.text}')


responseAddPokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json={ "pokemon_id": responseCreatePokemon.json()["id"] })
print(f'{responseAddPokeball.status_code}: {responseAddPokeball.text}')