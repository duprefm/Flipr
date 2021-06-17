FROM python:3.9.5-buster
RUN python3 -m pip install requests
# Create app directory
ENV SRC_DIR /usr/local/src/
VOLUME /usr/local/src/
WORKDIR ${SRC_DIR}
ADD Get_Token.py .
CMD [ "python3", "Get_Token.py" ]