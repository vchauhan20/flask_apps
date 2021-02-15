FROM python:3.6-buster
RUN mkdir /app
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
CMD gunicorn app:app --bind 0.0.0.0:$PORT --workers=2 thread=2 --reload
