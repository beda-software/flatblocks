FROM node:5.8
RUN npm install -g webpack
RUN npm install -g karma-cli

WORKDIR /app
ADD package.json ./package.json
RUN npm i
ADD . /app/user/
WORKDIR /app/user/
RUN npm run build
