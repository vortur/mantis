FROM node:16.10.0 as builder
WORKDIR /usr/src/app
COPY front/package.json front/package-lock.json ./
RUN npm install
COPY ./front ./
RUN npm run build

FROM nginx:1.19-alpine
COPY --from=builder /usr/src/app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
