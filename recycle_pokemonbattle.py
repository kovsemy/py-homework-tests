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

bodyAddPokeball = {
    "pokemon_id": "string"
}

paramsIsLiveOurPokemon = {
    "pokemon_id": "string"
}

paramsMyAlivePokemons = {
    "trainer_id": "37502",
    "status": 1
}

paramsEnemyPokemon = {
    "in_pokeball": 1,
    "status": 1
}

bodyStartBattle = {
  "attacking_pokemon": "string",
  "defending_pokemon": "string"
}

# Возвращает своего покемона если он есть, если его нет, создает нового и добавляет в покебол
def checkMyAlivePokemons():
    responseGetMyAlivePokemons = requests.get(url=f'{URL}/pokemons', params=paramsMyAlivePokemons)

    if ("message" in responseGetMyAlivePokemons.json()): # У нас нет покемонов?
        newPokemonId = createPokemon()
        addPokeboll(newPokemonId)
        return newPokemonId
    else: # иначе получаем покемона, который есть
        print('У меня есть покемон с именем - ' + responseGetMyAlivePokemons.json()["data"][0]["name"])
        return responseGetMyAlivePokemons.json()["data"][0]["id"] # Возвращаем id существующего покемона


def createPokemon():
    responseCreatePokemon = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=bodyCreatePokemon)
    print(str(responseCreatePokemon.status_code) + ', ' + responseCreatePokemon.text)
    return responseCreatePokemon.json()['id'] # get our pok


def addPokeboll(pokemon_id):
    bodyAddPokeball["pokemon_id"] = pokemon_id # change json to current pok
    responseAddPokeboll = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=bodyAddPokeball)
    print(str(responseAddPokeboll.status_code) + ', ' + responseAddPokeboll.text)


# Ищем себе вражеского покемона, который будет не с нашим trainer_id и атакой как наша+1, либо меньше, если находим, деремся, не находим завершаем программу
def getEnemyPokemons(myCurrentPok):
    repsoneGetEnemyPokemon = requests.get(url=f'{URL}/pokemons', params=paramsEnemyPokemon) # получаем список живых покемонов
    myCurrentPokAttack = requests.get(url=f'{URL}/pokemons', params={ "pokemon_id": myCurrentPok }).json()["data"][0]["attack"] # получаем атаку моего покемона

    for i in range(len(repsoneGetEnemyPokemon.json()["data"])):
        if (repsoneGetEnemyPokemon.json()["data"][i]["trainer_id"] == '37502'):
            i += 1
        if (myCurrentPokAttack >= repsoneGetEnemyPokemon.json()["data"][i]["attack"] or repsoneGetEnemyPokemon.json()["data"][i]["attack"] <= 2):
            enenemy = repsoneGetEnemyPokemon.json()["data"][i]["id"]
            print(f'enemy id is {enenemy}')
            return enenemy
        else:
            print('Равный покемон пока не найден')
            i += 1
    
    print('Забей, драться не с кем')
    return 0


def startBattle(our_pokemon_id, enemy_pokemon_id):
    bodyStartBattle["attacking_pokemon"] = our_pokemon_id
    bodyStartBattle["defending_pokemon"] = enemy_pokemon_id
    responseStartBattle = requests.post(url=f'{URL}/battle', headers=HEADER, json=bodyStartBattle)
    print(str(responseStartBattle.status_code) + ', ' + responseStartBattle.text)


# Запуск
currentPokemonId = checkMyAlivePokemons() # 
paramsIsLiveOurPokemon["pokemon_id"] = currentPokemonId
responseIsLive = requests.get(url=f'{URL}/pokemons', params=paramsIsLiveOurPokemon).json()["data"][0]["status"]


while (responseIsLive == 1):
    print(f'My pokemon status is {responseIsLive}')
    enemyPokemonId = getEnemyPokemons(currentPokemonId)
    if (enemyPokemonId == 0):
        responseIsLive = 0
    else:
        startBattle(currentPokemonId, enemyPokemonId)
        responseIsLive = requests.get(url=f'{URL}/pokemons', params=paramsIsLiveOurPokemon).json()["data"][0]["status"]