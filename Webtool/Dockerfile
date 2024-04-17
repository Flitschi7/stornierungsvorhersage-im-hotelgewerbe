# Verwenden eines offiziellen Python-Runtime als Eltern-Image
FROM arm64v8/python:3.9-slim

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Systemabhängigkeiten installieren
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Kopieren der Abhängigkeitsliste in den Container
COPY requirements.txt /app/

# Installieren der Python-Bibliotheken
RUN pip install --no-cache-dir -r requirements.txt

# Kopieren des Inhalts deines Projekts in den Container
COPY . /app

# Deine App läuft wahrscheinlich auf Port 5000 (Standard für Flask)
EXPOSE 5000

# Befehl, der beim Start des Containers ausgeführt wird
CMD ["python", "main.py"]
