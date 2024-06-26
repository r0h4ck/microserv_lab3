FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY facade.py ./

EXPOSE 9000

CMD [ "python3", "facade.py" ]
