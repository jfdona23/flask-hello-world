FROM python:slim

WORKDIR /app

COPY app/* ./

RUN pip install -r requirements.txt

ENV HOST "0.0.0.0"
ENV PORT "5000"
ENV DEBUG "False"

ENTRYPOINT ["python", "/app/hello-world.py"]