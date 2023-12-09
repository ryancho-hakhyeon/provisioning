FROM node

RUN mkdir -p /backend/app

COPY todoapp/ /backend/app/

WORKDIR /backend/app
RUN npm install
# RUN npm install --save express mongoose

COPY start.sh /start.sh

EXPOSE 8080

CMD [ "/bin/bash", "/start.sh" ]