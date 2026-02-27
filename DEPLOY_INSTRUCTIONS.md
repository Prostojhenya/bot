# Инструкция по деплою на Vercel

## Вариант 1: Через веб-интерфейс Vercel (рекомендуется)

1. Зарегистрируйтесь на https://vercel.com
2. Подключите GitHub репозиторий
3. В настройках проекта добавьте Environment Variables:
   - `TELEGRAM_BOT_TOKEN` = ваш токен бота
   - `WEBHOOK_URL` = https://ваш-проект.vercel.app/api/webhook
   - `GOOGLE_SHEET_ID` = 14jQrrNey8fI_WTdqG2YAlcloNIBilwNOQ7JbEUMkHNc

4. Загрузите credentials.json:
   - Скопируйте содержимое credentials.json
   - Создайте переменную `GOOGLE_CREDENTIALS` со всем JSON содержимым
   - Измените код в api/webhook.py чтобы читать из переменной окружения

5. Задеплойте проект через Vercel Dashboard

6. После деплоя установите webhook:
   ```bash
   python set_webhook.py
   ```

## Вариант 2: Через CLI

1. Войдите в Vercel:
   ```bash
   vercel login
   ```

2. Задеплойте:
   ```bash
   vercel --prod
   ```

3. Добавьте переменные окружения через CLI:
   ```bash
   vercel env add TELEGRAM_BOT_TOKEN
   vercel env add WEBHOOK_URL
   ```

4. Установите webhook:
   ```bash
   python set_webhook.py
   ```

## Важно!

После деплоя обязательно запустите `python set_webhook.py` чтобы Telegram знал куда отправлять сообщения.

Проверить webhook можно командой:
```bash
curl https://api.telegram.org/bot<YOUR_TOKEN>/getWebhookInfo
```
