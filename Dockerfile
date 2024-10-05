FROM python:latest
WORKDIR home/bot
COPY . home/bot
RUN pip install -r home/bot/requirements.txt