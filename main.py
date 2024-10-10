
from config import API_KEY, API_SECRET
from api_handler import ApiHandler
from campaign_manager import CampaignManager

def main():
    # Inicializa a API handler
    api_handler = ApiHandler(api_key=API_KEY, api_secret=API_SECRET)

    # Configuração inicial de campanhas
    campaign_manager = CampaignManager(api_handler)
    campaign_manager.create_campaign()

if __name__ == "__main__":
    main()
