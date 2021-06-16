FROM nginx:latest
# Create app directory
ENV SRC_DIR /usr/share/nginx/html/
WORKDIR ${SRC_DIR}
COPY script.js ${SRC_DIR}
COPY style.css ${SRC_DIR}
COPY index.html ${SRC_DIR}
COPY data.json ${SRC_DIR}
EXPOSE 80