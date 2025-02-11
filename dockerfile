FROM python:3.10

ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirments.txt /code/
RUN pip install -r requirments.txt

COPY . /code/