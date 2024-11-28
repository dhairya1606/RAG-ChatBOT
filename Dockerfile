FROM python:3.10.12

RUN apt-get update

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["bash", "start.sh"]

EXPOSE 80
