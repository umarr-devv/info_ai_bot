# Шаблон для aiogram

### Стек

- Python
- PostgresSQL
- Docker

### Фреймворки и Библиотеки

- aiogram - фреймворк для TelegramBotAPI
- sqlalchemy (с asyncpg) - для асинхронного взаимодействия с БД
- alembic - для миграций

***

### Настройка и создание файла конфигурации

Все файлы настроек хранятся по умолчанию в директории __/config__.
Файл __config-example.yml__ - пример конфигурационного файлы

***

### Создание и запус бота через Docker

```
docker build . -t bot
docker-compose up
```

***

### Локальный запуск

Создание виртуального окружения и установка зависимостей

```
python3 -m venv venv
pip install -r requirements.txt
```

Запуск бота осуществляется через команду

```
python3 app.py
```
