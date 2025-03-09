FROM python:3.12.0-slim-bullseye

# Set working directory for all following in container commands
WORKDIR /usr/src/app

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV DEBUG=False
# ENV PG_CONN_STRING=${PG_CONN_STRING}
# ENV REDIS_ENDPOINT=${REDIS_ENDPOINT}
# ENV REDIS_PASSWORD=${REDIS_PASSWORD}
# ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
# ENV RABBITMQ_BROKER=${RABBITMQ_BROKER}
# ENV STRIPE_WEBHOOK_SECRET=${STRIPE_WEBHOOK_SECRET}
# ENV CORS_ALLOWED_ORIGINS=${CORS_ALLOWED_ORIGINS}

RUN apt-get update \
  && apt-get -y install gcc vim libpq-dev gunicorn3 curl --fix-broken \
  && apt-get clean

# Handle all necessary dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install App
COPY ./app .

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]