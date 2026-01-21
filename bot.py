from amadeus import Client
import requests
import os

# ====== CONFIGURAÇÕES VIA ENV ======
AMADEUS_KEY = os.getenv("AMADEUS_CLIENT_ID")
AMADEUS_SECRET = os.getenv("AMADEUS_CLIENT_SECRET")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

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

resposta = requests.post(url, json=payload)
print(resposta.text)

print("Mensagem enviada com sucesso!")
