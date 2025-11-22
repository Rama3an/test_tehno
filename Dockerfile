FROM python:3.11-slim

WORKDIR .

COPY requirements.txt .
COPY alembic .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000