FROM python:3.7
RUN mkdir /app
WORKDIR /app

COPY . /app
RUN ls /app
RUN pip install -r ./requirements.txt

CMD ["python", "/app/app.py"]

