import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TOKEN'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = "37503"

def test_getTrainersStatusCode():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200


def test_isMyTrainerId():
    response = requests.get(url=f'{URL}/trainers', params={ 'trainer_id': TRAINER_ID })
    assert response.json()["data"][0]["id"] == TRAINER_ID

