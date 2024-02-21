from api_requests import request_api_clients
import random


class TestApiClients:

    def test_login(self):
        name = "Jhon"
        email = f"valentin{random.randint(0, 999999)}@email.com"
        response = request_api_clients.login(name, email)
        assert response.status_code == 201, f"Actual: {response.status_code}, Expected: 201"
        assert "accessToken" in response.json().keys(), f"Token was not generated. Response: {response.json()}"


