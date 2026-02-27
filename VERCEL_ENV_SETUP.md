# Настройка переменных окружения в Vercel

## Шаг 1: Откройте настройки проекта

1. Зайдите на https://vercel.com/dashboard
2. Выберите ваш проект "bot"
3. Перейдите в Settings → Environment Variables

## Шаг 2: Добавьте переменные

### TELEGRAM_BOT_TOKEN
- Name: `TELEGRAM_BOT_TOKEN`
- Value: ваш токен бота (из .env файла)
- Environment: Production, Preview, Development

### GOOGLE_CREDENTIALS
- Name: `GOOGLE_CREDENTIALS`
- Value: скопируйте ВЕСЬ содержимое файла credentials.json (должно быть JSON)
- Environment: Production, Preview, Development

Пример содержимого credentials.json:
```json
{
  "type": "service_account",
  "project_id": "...",
  "private_key_id": "...",
  "private_key": "...",
  "client_email": "...",
  ...
}
```

### WEBHOOK_URL (добавьте после первого деплоя)
- Name: `WEBHOOK_URL`
- Value: `https://ваш-проект.vercel.app/api/webhook`
- Environment: Production, Preview, Development

## Шаг 3: Redeploy

После добавления переменных нажмите "Redeploy" в Vercel Dashboard

## Шаг 4: Установите webhook

После успешного деплоя выполните локально:

```bash
# Добавьте в .env
WEBHOOK_URL=https://ваш-проект.vercel.app/api/webhook

# Запустите
python set_webhook.py
```

## Проверка

Откройте в браузере: `https://ваш-проект.vercel.app/`
Должно показать: "Telegram Bot Webhook is running"
