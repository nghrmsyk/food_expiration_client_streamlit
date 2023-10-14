FROM python:3.11.5-slim-bullseye

WORKDIR /app

ENV SERVER_URL = http://localhost:8000

RUN apt update && apt -y upgrade

RUN pip install streamlit 
RUN pip install -U pydantic

COPY ./app/ /app/

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]