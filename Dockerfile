FROM python:3.12

WORKDIR /https://t.me/WebXBots

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY .Python.org .

CMD ["python3", "bot.py"]
