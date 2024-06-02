FROM python:3.11-slim-buster
LABEL authors="Viktor"

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID django_user
USER django_user

WORKDIR /home/django_user/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]