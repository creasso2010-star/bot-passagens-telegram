import os

# Vamos ver o que o GitHub Actions está lendo
print("TELEGRAM_TOKEN =", os.getenv("TELEGRAM_TOKEN"))
print("CHAT_ID =", os.getenv("CHAT_ID"))
print("AMADEUS_CLIENT_ID =", os.getenv("AMADEUS_CLIENT_ID"))
print("AMADEUS_CLIENT_SECRET =", os.getenv("AMADEUS_CLIENT_SECRET"))
