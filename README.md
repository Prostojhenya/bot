# Telegram Order Bot

Бот для обработки заявок на сборку и записи в Google Sheets.

## Деплой на Vercel

1. Импортируйте этот репозиторий на https://vercel.com/new
2. Добавьте переменные окружения:
   - `TELEGRAM_BOT_TOKEN`
   - `WEBHOOK_URL` (https://your-project.vercel.app/api/webhook)
3. Деплой произойдет автоматически
4. Запустите `python set_webhook.py` для установки webhook

## Локальный запуск

```bash
pip install -r requirements.txt
python bot.py
```

## Структура

- `bot.py` - основной бот (polling)
- `api/webhook.py` - webhook версия для Vercel
- `credentials.json` - Google Sheets credentials
