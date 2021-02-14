FROM python:alpine3.7
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["/app.py"]
EXPOSE 5000
CMD [ "python","app.py" ]
