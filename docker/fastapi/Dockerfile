FROM python:3.12
WORKDIR /usr/src/app
COPY ./src/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 80 --reload --log-level ${UVICORN_LOG_LEVEL:-info}"]
