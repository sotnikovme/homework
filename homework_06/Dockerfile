FROM python:3.10-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY /app /app

#EXPOSE 5000

#CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["python", "main.py"]
