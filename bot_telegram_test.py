import os
import requests

# Ler os secrets do GitHub Actions
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

mensagem = "✅ Teste do bot Telegram funcionando pelo GitHub Actions!"

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": mensagem
}

resposta = requests.post(url, json=payload)
print("Resposta da API do Telegram:", resposta.text)
