# app/Dockerfile

FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY ./config/ ./streamlit/config/
COPY ./app/ ./streamlit/app/

RUN pip3 install -r ./streamlit/config/requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "./streamlit/app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
