
from api_handler import ApiHandler

class CampaignManager:
    def __init__(self, api_handler: ApiHandler):
        self.api_handler = api_handler

    def create_campaign(self):
        # Exemplo de criação de campanha
        data = {
            'name': 'Minha Campanha',
            'budget': 1000,
            'target': 'público-alvo'
        }
        response = self.api_handler.make_request('https://api.exemplo.com/campaigns', data)
        print(f'Campanha criada: {response}')
