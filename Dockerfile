# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /usr/src/circles

COPY circle.py /usr/src/circles
COPY bg.jpg /usr/src/circles
COPY mask.png /usr/src/circles
COPY requirements.txt /usr/src/circles
RUN pip install --no-cache-dir -r /usr/src/circles/requirements.txt

COPY . .

#ENTRYPOINT ["/bin/bash"]
CMD [ "python", "/usr/src/circles/circle.py" ]