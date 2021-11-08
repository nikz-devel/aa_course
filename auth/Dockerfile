FROM python:3.8

WORKDIR /app

RUN pip install pipenv

COPY . .

RUN pipenv install --system --deploy

WORKDIR /app/src

CMD ["./manage.py", "runserver", "0.0.0.0:5000"]

