FROM python:3.7.9
LABEL authors="raraj"

WORKDIR /Annotgo

COPY ./requirements.txt ./
COPY ./icons ./icons
COPY ./libs ./libs
COPY ./Annot_UI.py ./
COPY ./libs ./libs


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./Annot_UI.py", "--host", "0.0.0.0", "--port", "80"]