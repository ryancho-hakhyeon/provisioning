FROM node:14 AS builder
# FROM node:18 AS builder

RUN mkdir -p /app/src

COPY public/ /app/src/

WORKDIR /app/src
RUN npm install  

FROM nginx:latest
COPY --from=builder /app/src /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]