FROM python:3.11.5-slim-bullseye

WORKDIR /app

RUN apt update && apt -y upgrade

RUN pip install streamlit 
RUN pip install -U pydantic

ENV SERVER_IP=host.docker.internal:8000

COPY ./app/ /app/

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]