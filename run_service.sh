docker build . -f service.Dockerfile -t hddservice:latest
docker run --rm -it -v "$(pwd)/kuku:/app/data" hddservice