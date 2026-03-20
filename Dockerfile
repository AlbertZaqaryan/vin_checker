FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

# файл уже должен быть в проекте
COPY s3_token.txt /app/s3_token.txt

CMD [ "python", "code.py" ]