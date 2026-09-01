FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt-get/lists/*

WORKDIR /home/myapp
COPY backend/requirements.txt .
RUN pip install -r requirements.txt 
COPY . .
EXPOSE 5050
CMD ["python3", "sample_app.py"]