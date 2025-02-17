FROM python:3.12

WORKDIR /code

ENV DEEPSEEK_HOST_URL="http://172.18.0.2:11434"

ARG MODEL_NAME="deepseek-coder:6.7b"

ENV MODEL_NAME=$MODEL_NAME

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "8080"]