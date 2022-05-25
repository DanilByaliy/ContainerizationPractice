FROM node:16-alpine as build
 
WORKDIR /app
 
COPY package*.json .
 
RUN npm i
 
COPY . .
 
FROM gcr.io/distroless/nodejs:16

WORKDIR /app
 
COPY --from=build /app /app
 
CMD ["index.js"]