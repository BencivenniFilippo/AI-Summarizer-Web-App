# Usa l'immagine base di Python
FROM python:3.13.1

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia il file requirements.txt e installa le dipendenze
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il codice del progetto nel container
COPY . /app/

# Esegui l'app con Gunicorn (o Flask per il dev)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.__init__:app"]