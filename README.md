# Flipr
Scripts Flipr persos pour ma piscine

## web 
docker build -t flipr-webserver:latest . 

docker volume create FLIPR

docker run -d -p 8080:80 -v FLIPR:/usr/share/nginx/html/ flipr-webserver:latest

docker exec -it <connt_name> /bin/bash

## python
docker build -t flipr-getdata:latest .

docker run -d -v FLIPR:/usr/local/src/ flipr-getdata:latest
