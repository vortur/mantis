FROM node:16.10.0

WORKDIR /strapi

ADD strapi/package.json .
ADD strapi/package-lock.json .
RUN ls -la
RUN npm install

ADD strapi ./

RUN npm run build

EXPOSE 1337

CMD ["npm", "start"]