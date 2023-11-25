FROM python:3.7.9
LABEL authors="raraj"

WORKDIR /Annotgo

COPY ./requirements.txt ./
COPY ./src ./src

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./src/main.py", "--host", "0.0.0.0", "--port", "80"]