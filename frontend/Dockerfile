FROM node:13.7.0-alpine

WORKDIR /app/
ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json ./
RUN npm install
RUN npm install react-scripts@3.0.1 -g
RUN npm install serve -g

CMD ["npm", "start"]