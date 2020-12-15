FROM python:3

ADD nerdocalire.py /

RUN pip install python-telegram-bot

CMD [ "python", "./RubberDuckDebuggerBot.py" ]