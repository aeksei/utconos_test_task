FROM tiangolo/uvicorn-gunicorn:python3.8-slim
ENV BACKEND_APP_DIR=/app

COPY requirements.txt $BACKEND_APP_DIR/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r $BACKEND_APP_DIR/requirements.txt

COPY . $BACKEND_APP_DIR
