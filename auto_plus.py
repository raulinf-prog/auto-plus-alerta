raise Exception("PRUEBA: ESTOY EJECUTANDO ESTE ARCHIVO")
import requests
import os

print("🚀 ESTOY EJECUTANDO ESTE ARCHIVO")

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

respuesta = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "✅ Prueba: GitHub Actions + Telegram funciona"
    }
)

print("Código:", respuesta.status_code)
print("Respuesta Telegram:", respuesta.text)
