# Базовый образ с Python
FROM python:3.12-slim

# Рабочая папка внутри контейнера
WORKDIR /app

# Копируем приложение в образ
COPY app/ /app/

# Проверяем, что в коде нет синтаксических ошибок
RUN python -m py_compile /app/app.py && echo "Syntax check passed"

# Приложение слушает порт 8000
EXPOSE 8000

# Команда запуска контейнера
CMD ["python", "-u", "app.py"]
