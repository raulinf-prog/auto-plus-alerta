import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.mintur.gob.es/PortalAyudas/programa-auto/Paginas/Index.aspx"

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

ESTADO = "estado.txt"


def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    respuesta = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": mensaje
        }
    )

    print("Telegram:", respuesta.status_code)
    print(respuesta.text)


def comprobar_auto_plus():

    print("🔎 Comprobando Auto+...")

    r = requests.get(
        URL,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("Página:", r.status_code)

    texto = BeautifulSoup(
        r.text,
        "html.parser"
    ).get_text(" ").lower()

    palabras_apertura = [
        "plazo abierto",
        "presentación de solicitudes",
        "solicitud abierta",
        "se inicia el plazo",
        "abierto el plazo"
    ]

    for palabra in palabras_apertura:
        if palabra in texto:
            print("✅ Detectada palabra:", palabra)
            return True

    print("❌ No parece abierto")
    return False


def leer_estado():

    if os.path.exists(ESTADO):
        with open(ESTADO, "r") as f:
            return f.read().strip()

    return "cerrado"


def guardar_estado(valor):

    with open(ESTADO, "w") as f:
        f.write(valor)


# -----------------------------

abierto = comprobar_auto_plus()
estado_actual = leer_estado()

if abierto and estado_actual != "abierto":

    enviar_telegram(
        "🚗 AUTO+ DISPONIBLE\n\n"
        "Parece que el plazo de solicitud está abierto.\n\n"
        f"Consulta aquí:\n{URL}"
    )

    guardar_estado("abierto")


elif not abierto:

    guardar_estado("cerrado")
    print("Estado guardado: cerrado")


else:

    print("Ya se avisó anteriormente.")
