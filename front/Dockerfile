# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем требования
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app

# Открываем порт, на котором будет работать Streamlit
EXPOSE 8501

# Запуск приложения
CMD ["streamlit", "run", "app.py"]