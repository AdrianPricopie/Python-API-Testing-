import requests
import random


# metoda ajutatoare pentru order api
def get_token():
    body = {
        "clientName": "Test",
        "clientEmail": f"dummy_emailx{random.randint(0, 999999)}@email.com"
    }
    response = requests.post("https://simple-books-api.glitch.me/api-clients", json=body)
    return response.json()['accessToken']


def login(client_name, client_email):
    body = {
        "clientName": client_name,
        "clientEmail": client_email
    }
    return requests.post("https://simple-books-api.glitch.me/api-clients", json=body)

print(get_token())


