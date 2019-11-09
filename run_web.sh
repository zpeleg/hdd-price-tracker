docker build . -f web.Dockerfile -t hddweb:latest
docker run --rm -it -v "$(pwd)/kuku:/app/data" -p 8080:80 -d hddweb