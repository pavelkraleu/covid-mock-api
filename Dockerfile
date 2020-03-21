FROM python:3.8-slim-buster

COPY ./requirements.txt /
RUN pip install -r /requirements.txt

COPY ./api /api

WORKDIR /api

ENTRYPOINT ["python3", "app.py"]
