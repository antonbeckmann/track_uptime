# Verwende das offizielle Python-Basisimage
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis innerhalb des Containers
WORKDIR /app

# Kopiere die Anforderungen (requirements) in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Anforderungen
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Python-Code in das Arbeitsverzeichnis
COPY app.py .

# Führe das Python-Programm aus, wenn der Container gestartet wird
CMD [ "python", "app.py" ]
