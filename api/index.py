import os
import re
import json
import requests
from http.server import BaseHTTPRequestHandler

import gspread
from google.oauth2.service_account import Credentials


# ================= ЗАГРУЗКА ПЕРЕМЕННЫХ =================

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8551219311:AAFhc1mI0snOy2JEXXuTl3fZFtMp00exvXw")

GOOGLE_SHEET_ID = "14jQrrNey8fI_WTdqG2YAlcloNIBilwNOQ7JbEUMkHNc"


# ================= GOOGLE SHEETS =================

def get_worksheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    google_creds = os.getenv("GOOGLE_CREDENTIALS")
    
    if google_creds:
        creds_dict = json.loads(google_creds)
        credentials = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    else:
        credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(GOOGLE_SHEET_ID)
    worksheet = spreadsheet.sheet1
    return worksheet


# ================= ВСПОМОГАТЕЛЬНЫЕ =================

def clean_number(value: str):
    if not value:
        return ""
    return value.replace(" ", "").replace(" ", "").strip()


def split_fio(fio: str):
    parts = fio.strip().split()
    last_name = parts[0] if len(parts) > 0 else ""
    first_name = parts[1] if len(parts) > 1 else ""
    middle_name = parts[2] if len(parts) > 2 else ""
    return last_name, first_name, middle_name


def parse_order(text: str):
    data = {}

    number_match = re.search(r"Заявка на сборку №:\s*(\d+)", text)
    phone_match = re.search(r"Телефон:\s*(\d+)", text)
    fio_match = re.search(r"ФИО:\s*(.+)", text)
    address_match = re.search(r"Адрес:\s*(.+)", text)
    item_match = re.search(r"Изделие\s+(.+)", text)
    assembly_sum_match = re.search(r"Сумма сборки\s+([\d\s ]+)", text)

    data["number"] = number_match.group(1) if number_match else ""
    data["phone"] = phone_match.group(1) if phone_match else ""
    data["fio"] = fio_match.group(1).strip() if fio_match else ""
    data["address"] = address_match.group(1).strip() if address_match else ""
    data["item"] = item_match.group(1).strip() if item_match else ""
    data["assembly_sum"] = clean_number(assembly_sum_match.group(1)) if assembly_sum_match else ""

    return data


def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, json=data, timeout=10)
    except:
        pass


def handle_message(message):
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")
    
    if not chat_id:
        return
    
    if text == "/start":
        send_message(chat_id, "Отправьте текст заявки.")
        return
    
    if "Заявка на сборку №" not in text:
        send_message(chat_id, "Это не заявка.")
        return
    
    parsed = parse_order(text)
    last_name, first_name, middle_name = split_fio(parsed["fio"])
    
    try:
        worksheet = get_worksheet()
        
        phone_with_8 = "8" + parsed["phone"]
        worksheet.update("F16", phone_with_8)
        worksheet.update("G16", last_name)
        worksheet.update("G17", first_name)
        worksheet.update("G18", middle_name)
        worksheet.update("G19", parsed["number"])
        worksheet.update("H16:L16", [[parsed["address"], "", "", "", ""]])
        worksheet.update("M16:O16", [[parsed["item"], "", ""]])
        worksheet.update("P16", parsed["assembly_sum"])
        
        send_message(chat_id, f"Заявка №{parsed['number']} записана.")
    except Exception as e:
        send_message(chat_id, f"Ошибка: {str(e)}")


# ================= VERCEL HANDLER =================

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            update = json.loads(post_data.decode('utf-8'))
            
            if "message" in update:
                handle_message(update["message"])
            
            self.send_response(200)
            self.end_headers()
            
        except Exception as e:
            print(f"Error: {e}")
            self.send_response(200)
            self.end_headers()
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Telegram Bot Webhook is running! Ready to receive orders.")
