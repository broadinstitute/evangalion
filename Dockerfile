FROM python:3.3

WORKDIR /app
COPY app /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

