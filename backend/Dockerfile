FROM python

LABEL maintainer="devpeskov@proton.me"

WORKDIR /code

RUN pip install poetry

COPY . /code/

RUN poetry config virtualenvs.create false \
  && poetry install --only main

CMD ["python", "main.py"]
