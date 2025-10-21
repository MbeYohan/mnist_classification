Utiliser une image de base Python
FROM python:3.9-slim

Définir le répertoire de travail
WORKDIR /app

Copier les dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

Copier le reste de l'application
COPY . .

Exposer le port de l'application Flask
EXPOSE 5000

Lancer l'application
CMD ["python", "app.py"]
