#FROM node:17.2-bullseye-slim
FROM node:lts-alpine
COPY ./blog /blog
WORKDIR /blog
RUN yarn install
EXPOSE 8080
CMD ["yarn", "serve"]
