FROM python:3.10.8-slim-buster
RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip install -U pip && pip3 install -U -r requirements.txt
WORKDIR /punisher-303

COPY . .
CMD ["python", "bot.py"]
