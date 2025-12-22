FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV APP_ENV=dev
ENV APP_NAME="My First DevOps App"

EXPOSE 5001

CMD ["python", "app.py"]
