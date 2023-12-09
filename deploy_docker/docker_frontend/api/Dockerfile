FROM python:3.8

RUN apt-get update

RUN useradd -m -d /api api
USER api

WORKDIR /api/
COPY requirements.txt /api/src/
RUN pip install -r /api/src/requirements.txt

COPY todoapp/ /api/src/

WORKDIR /api/src

COPY info.txt /api/src/

EXPOSE 5000

CMD ["/api/.local/bin/gunicorn", "-b", "0.0.0.0:5000", "web:app"]


