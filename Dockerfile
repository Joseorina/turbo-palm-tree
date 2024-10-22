FROM python:3.7.3

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python", "main.py" ]
