FROM python:3.6
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install vim -y

ADD . /app/
CMD ["python", "-m", "service.scrape_price", "/app/data"]