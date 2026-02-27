# Альтернативные способы деплоя

## Вариант 1: Railway (проще чем Vercel)

1. Зарегистрируйтесь на https://railway.app
2. Создайте новый проект "Deploy from GitHub repo"
3. Добавьте переменные окружения
4. Railway автоматически задеплоит бота
5. Запустите `python set_webhook.py` с вашим Railway URL

## Вариант 2: Render.com (бесплатный)

1. Зарегистрируйтесь на https://render.com
2. Создайте новый "Web Service"
3. Подключите GitHub репозиторий
4. Укажите команду запуска: `python -m http.server` (для webhook)
5. Добавьте переменные окружения
6. Запустите `python set_webhook.py`

## Вариант 3: Локальный сервер + ngrok (для тестирования)

1. Установите ngrok: https://ngrok.com/download
2. Запустите бота локально
3. В другом терминале: `ngrok http 8000`
4. Скопируйте HTTPS URL из ngrok
5. Установите webhook с этим URL

## Вариант 4: PythonAnywhere (бесплатный)

1. Зарегистрируйтесь на https://www.pythonanywhere.com
2. Загрузите файлы проекта
3. Настройте Flask/FastAPI приложение для webhook
4. Установите webhook

## Рекомендация: Railway

Railway самый простой для Python ботов:
- Автоматический деплой из GitHub
- Бесплатный тариф
- Поддержка Python из коробки
- Простая настройка переменных окружения
