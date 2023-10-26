FROM python:3.9
WORKDIR /app
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./src/* /app/