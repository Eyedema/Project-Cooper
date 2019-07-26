FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN chmod 644 /code/app.py
RUN pip install flask
RUN pip install mysql-connector-python
CMD ["python", "app.py"]
EXPOSE 5000
