# syntax=docker/dockerfile:1
FROM python:3.11
WORKDIR /futur-flask
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [“python”, “run.py”]