FROM python:3.8

WORKDIR /app

RUN pip install pipenv

COPY . .

RUN pipenv install --system --deploy

WORKDIR /app/src

RUN ./manage.py collectstatic
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "project.wsgi"]

