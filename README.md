# Flipr
Scripts Flipr persos pour ma piscine

## web 
docker build -t flipr-webserver:latest . 

docker volume create FLIPRWEB

docker run -d -p 8080:80 -v FLIPRWEB:/usr/share/nginx/html/ -v FLIPPYTHON:/usr/local/src/ flipr-webserver:latest

docker exec -it <connt_name> /bin/bash

## python
docker build -t flipr-getdata:latest .

docker volume create FLIPPYTHON

docker run -d -v FLIPPYTHON:/usr/local/src/ flipr-getdata:latest
