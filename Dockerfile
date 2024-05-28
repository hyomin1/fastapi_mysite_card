FROM tiangolo/uvicorn-gunicorn:python3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade && pip install -r /app/requirements.txt

EXPOSE 8000

COPY ./ /app/

CMD 