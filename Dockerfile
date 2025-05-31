FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app/ app/
COPY model/ model/
COPY src/ src/

EXPOSE 5000

CMD ["python", "app/app.py"]

