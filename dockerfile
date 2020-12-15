FROM python:3

ADD RubberDuckDebuggerBot.py /

RUN pip install python-telegram-bot

CMD [ "python", "./RubberDuckDebuggerBot.py" ]