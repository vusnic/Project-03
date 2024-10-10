
import requests

class ApiHandler:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def make_request(self, endpoint, data):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(endpoint, json=data, headers=headers)
        return response.json()

    # Outros métodos de integração com a API
