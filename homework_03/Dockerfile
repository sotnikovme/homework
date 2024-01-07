#docker build -t hw03 .
#docker run --rm -p 8000:8000 hw03

FROM python:3.9-buster

WORKDIR /

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0" ,"--port=8000"]
