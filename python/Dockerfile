FROM python:3.9.5-buster
RUN python3 -m pip install requests
# Create app directory
ENV SRC_DIR /usr/share/nginx/html/
WORKDIR ${SRC_DIR}
ADD Get_Token.py .
CMD [ "python3", "Get_Token.py" ]

#FROM nginx:latest
#RUN apt-get install python3 python-pip
# Create app directory
#ENV SRC_DIR /usr/share/nginx/html/
#WORKDIR ${SRC_DIR}
#ADD Get_Token.py .
#ADD index.html .
#EXPOSE 80