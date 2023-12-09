FROM nginx:latest

# RUN useradd -m -d /www-data www-data
USER www-data

COPY public/ /www-data/web
COPY default.conf.template /etc/nginx/templates/default.conf.template

USER root
RUN service nginx restart

EXPOSE 80