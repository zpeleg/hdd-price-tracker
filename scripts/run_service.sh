docker build .. -f service.Dockerfile -t hallo
docker run --rm -it -v "$(pwd)/kuku:/app/data" hallo