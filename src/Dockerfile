FROM python:3.11.2-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
  && apt install -y netcat make \
  && pip install --upgrade pip \
  && pip install poetry==1.4.2

COPY ./src/pyproject.toml ./src/poetry.lock ./

ARG DEV_DEPS=False

RUN poetry config virtualenvs.create false
RUN if [ $DEV_DEPS = True ] ; then \
  poetry install --no-interaction --no-ansi ; else \
  poetry install --only main --no-interaction --no-ansi ; fi

COPY . .

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "src/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]