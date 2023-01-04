FROM python

LABEL maintainer="devpeskov@proton.me"

WORKDIR /code

RUN pip install poetry

RUN apt-get update \
  && apt-get install -y netcat \
  && rm -rf /var/lib/apt/lists/*

COPY . /code/

RUN poetry config virtualenvs.create false \
  && poetry install --only main

ENTRYPOINT ["/code/boot.sh"]
