FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

ENV PYTHONPATH /app

RUN pip3 install -r requirements.txt
RUN pip3 install .


CMD [ "streamlit", "run", "preprocessor/preprocess.py"]
