FROM python:3.6-slim
RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

COPY requirements.txt .
RUN pip install -r requirements.txt --src /usr/local/src

COPY web/nginx.conf /etc/nginx
COPY ./web /srv/flask_app
WORKDIR /srv/flask_app
RUN chmod +x ./start.sh

CMD ["./start.sh"]
