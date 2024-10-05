FROM python:latest
WORKDIR home/info_ai_bot
COPY . home/info_ai_bot
RUN pip install -r home/info_ai_bot/requirements.txt