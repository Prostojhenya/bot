# Деплой бота на Vercel

## Шаги:

1. Установите Vercel CLI:
```bash
npm i -g vercel
```

2. Добавьте в `.env` переменную WEBHOOK_URL:
```
WEBHOOK_URL=https://your-app.vercel.app/api/webhook
```

3. Загрузите credentials.json в Vercel как файл или переменную окружения

4. Задеплойте проект:
```bash
vercel
```

5. После деплоя установите webhook:
```bash
python set_webhook.py
```

6. Проверьте webhook:
```bash
curl https://your-app.vercel.app/api/webhook
```

## Переменные окружения в Vercel:

В настройках проекта на Vercel добавьте:
- TELEGRAM_BOT_TOKEN
- WEBHOOK_URL
- Содержимое credentials.json (можно как JSON строку в переменную GOOGLE_CREDENTIALS)

## Примечание:

Vercel использует serverless функции, поэтому каждый запрос обрабатывается отдельно.
Это идеально для webhook-ботов.
