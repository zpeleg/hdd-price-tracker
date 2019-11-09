FROM python:3.6
ADD requirements.txt /app/
WORKDIR /
RUN pip install -r /app/requirements.txt
RUN apt-get update
RUN apt-get install vim -y

ADD . /app/
CMD ["python", "-m", "app.service.scrape_price", "/app/data"]