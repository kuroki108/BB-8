FROM python:3.13-slim

WORKDIR /app

# pip aktualisieren
RUN python -m pip install --upgrade pip

# requirements installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Projekt kopieren
COPY . .

# Bot starten (expects DISCORD_TOKEN from environment or .env)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD ["python", "script.py"]
