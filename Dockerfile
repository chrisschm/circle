# syntax=docker/dockerfile:1
FROM python:3-slim

LABEL version="0.0.1"
LABEL author="Christian Schmidt"

WORKDIR /usr/src/circles

COPY circle.py /usr/src/circles
COPY bg.jpg /usr/src/circles
COPY mask.png /usr/src/circles
COPY requirements.txt /usr/src/circles
RUN pip install --no-cache-dir -r /usr/src/circles/requirements.txt

COPY . .

ENTRYPOINT ["python", "/usr/src/circles/circle.py"]
