FROM python:3.6-slim
RUN apt-get clean \
    && apt-get -y update \
    && apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && apt-get -y install vim

COPY requirements.txt .
RUN pip install -r requirements.txt --src /usr/local/src

COPY ./web/nginx.conf /etc/nginx
COPY . /srv/flask_app
WORKDIR /srv/flask_app
RUN chmod +x ./web/start.sh

CMD ["./web/start.sh"]
