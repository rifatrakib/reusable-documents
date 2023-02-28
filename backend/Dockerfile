FROM python:3.9 as requirements-stage

WORKDIR /tmp

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./build /code/build
COPY ./dist /code/dist
COPY ./pydantic_mongo_reusables.egg-info /code/pydantic_mongo_reusables.egg-info
RUN pip install /code/dist/pydantic_mongo_reusables-0.1.2-py3-none-any.whl

COPY ./server /code/server

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
