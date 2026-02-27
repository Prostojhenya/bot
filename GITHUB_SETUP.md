# Быстрая настройка GitHub

## Шаг 1: Создайте репозиторий на GitHub

1. Откройте: https://github.com/new
2. Название: `telegram-order-bot`
3. Сделайте ПРИВАТНЫМ (важно для безопасности!)
4. НЕ добавляйте README, .gitignore
5. Нажмите "Create repository"

## Шаг 2: Подключите локальный проект

После создания репозитория GitHub покажет команды. Выполните их:

```bash
git remote add origin https://github.com/ВАШ_USERNAME/telegram-order-bot.git
git branch -M main
git push -u origin main
```

Или если у вас SSH:

```bash
git remote add origin git@github.com:ВАШ_USERNAME/telegram-order-bot.git
git branch -M main
git push -u origin main
```

## Шаг 3: Деплой на Vercel

1. Откройте: https://vercel.com/new
2. Импортируйте репозиторий `telegram-order-bot`
3. Добавьте Environment Variables:
   - `TELEGRAM_BOT_TOKEN`
   - `WEBHOOK_URL` (получите после первого деплоя)
4. Нажмите "Deploy"

## Готово!

После деплоя:
1. Скопируйте URL проекта (например: https://telegram-order-bot.vercel.app)
2. Добавьте в .env: `WEBHOOK_URL=https://telegram-order-bot.vercel.app/api/webhook`
3. Запустите: `python set_webhook.py`

Бот готов к работе!
