FROM python:3.10-slim

WORKDIR /app

RUN pip install numpy

COPY ./hello.py .

CMD [ "python", "hello.py" ]