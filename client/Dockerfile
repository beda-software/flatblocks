FROM node:5.8
RUN npm install -g webpack@~1.12.13
RUN npm install -g concurrently@~2.0.0
RUN npm install -g webpack-dev-server@~1.14.1
RUN npm install -g just-wait@~1.0.5
RUN npm install -g forever@~0.15.1
RUN npm install -g karma-cli
WORKDIR /app
ADD package.json ./package.json
RUN npm i
ADD . /app/user/
WORKDIR /app/user/
RUN npm run build

