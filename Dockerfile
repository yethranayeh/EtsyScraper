# Better build time
FROM python:3.7-slim-stretch

# Smaller image size
# FROM python:3.7-alpine


# /USE WITH DOCKER-COMPOSE

ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

# USE WITH DOCKER-COMPOSE/


# /USE WITHOUT DOCKER-COMPOSE

# WORKDIR /app
# COPY requirements.txt .
# RUN pip3 install --user -r requirements.txt
# COPY . .
# CMD cd EtsyScraper ; python3 manage.py runserver 0.0.0.0:8000

# USE WITHOUT DOCKER-COMPOSE/
