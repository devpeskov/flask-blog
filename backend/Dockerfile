FROM python

WORKDIR /code

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /code/

RUN poetry config virtualenvs.create false \
  && poetry install

CMD ["python", "main.py"]
