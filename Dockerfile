FROM python:3.8

RUN pip install pipenv

WORKDIR /app
ADD Pipfile Pipfile.lock ./
ADD .env ./
RUN pipenv install --dev

COPY api/ ./api/

EXPOSE 5000
