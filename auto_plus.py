import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.mintur.gob.es/PortalAyudas/programa-auto/Paginas/Index.aspx"

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def enviar_telegram(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": texto
        }
    )


def comprobar():

    r = requests.get(
        URL,
        timeout=20
    )

    texto = BeautifulSoup(
        r.text,
        "html.parser"
    ).get_text().lower()

    palabras = [
        "solicitud",
        "plazo abierto",
        "presentación",
        "abierto"
    ]

    for palabra in palabras:
        if palabra in texto:
            return True

    return False


if comprobar():

    enviar_telegram(
        "🚗 AUTO+ PUEDE ESTAR ABIERTO\n\n"
        "Revisa la convocatoria:"
        "\n" + URL
    )

else:
    print("Todavía cerrado")
    enviar_telegram(
        "🚗 AUTO+ PUEDE ESTAR ABIERTO\n\n"
        "Revisa la convocatoria:"
        "\n" + URL
