# Используйте официальный образ Python
FROM python:3.9

# Установите зависимости
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Скопируйте код приложения
COPY . /app

# Укажите порт, который будет слушать ваше приложение
# EXPOSE 8000

# Запустите FastAPI приложение
# CMD ["uvicorn", "main:app", "--reload"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# docker run  --name mycontainer9 -p 80:80 myimage9
# docker build -t myimage9 .