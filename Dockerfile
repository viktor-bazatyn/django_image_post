FROM python:3.11-slim-buster
LABEL authors="Viktor"


WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["gunicorn", "base.wsgi:application", "--bind", "0.0.0.0:8000"]