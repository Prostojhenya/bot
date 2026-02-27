import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # https://your-app.vercel.app/api/webhook

if not BOT_TOKEN or not WEBHOOK_URL:
    print("Ошибка: TELEGRAM_BOT_TOKEN или WEBHOOK_URL не найдены в .env")
    exit(1)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook"
data = {"url": WEBHOOK_URL}

response = requests.post(url, json=data)
print(response.json())
