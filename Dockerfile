FROM python:3.10.0-alpine
RUN pip install passlib
RUN pip install argon2_cffi
RUN pip install bcrypt
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "app.ApiJanuaryProject:app", "--host", "0.0.0.0", "--port", "8000"]
