# Build stage
FROM node:18 as build

WORKDIR /app
COPY package.json .
RUN npm install

COPY . .
RUN npm run build

# Serve via nginx
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Optional: custom nginx config