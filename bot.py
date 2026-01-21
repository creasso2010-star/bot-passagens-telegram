from amadeus import Client
import requests

# ====== CONFIGURAÇÕES ======
AMADEUS_KEY = "zO7S04CFEAsguyQIfa79213eO46PwMLp"
AMADEUS_SECRET = "oq0Sn9G8j4LAt1OD"

TELEGRAM_TOKEN = "8543963799:AAFtKzc_4zfIhw8tfNcodSTFc238LJvhiPA"
CHAT_ID = "858610936"

# ====== AMADEUS ======
amadeus = Client(
    client_id=AMADEUS_KEY,
    client_secret=AMADEUS_SECRET
)

# Exemplo: GRU → GIG
response = amadeus.shopping.flight_offers_search.get(
    originLocationCode="GRU",
    destinationLocationCode="GIG",
    departureDate="2026-02-15",
    adults=1,
    currencyCode="BRL",
    max=1
)

preco = response.data[0]['price']['total']

mensagem = f"""
✈️ Teste de busca

Origem: GRU
Destino: GIG
Data: 15/02/2026
Preço: R$ {preco}
"""

# ====== TELEGRAM ======
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": mensagem
}

requests.post(url, json=payload)

print("Mensagem enviada com sucesso!")