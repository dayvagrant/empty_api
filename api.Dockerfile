FROM python:3.8

RUN apt-get update
RUN apt-get autoclean

ENV DOCKER=true

RUN pip install --upgrade pip
RUN pip install poetry


COPY pyproject.toml .
RUN poetry install

COPY app app
RUN .env .env

EXPOSE 2205
CMD ["poetry","run", "uvicorn", "app.application:APP", "--host", "0.0.0.0", "--port", "2205", "--reload"]
