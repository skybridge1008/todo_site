FROM python:3.9-alpine3.13

RUN pip3 install django

WORKDIR /usr/src/app

COPY . .

WORKDIR ./todosite

CMD ["python3", "manage.py", "runserver", "0:8000"]

EXPOSE 8000