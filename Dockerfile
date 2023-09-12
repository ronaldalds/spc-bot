FROM selenium/standalone-chrome:latest

USER root

ENV TZ=America/Fortaleza

# Instala o Python, pip e xvfb
RUN apt-get update && apt-get install -y python3 python3-pip xvfb

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD xvfb-run --server-args="-screen 0 1280x960x24" python3 main.py

# docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" <container>