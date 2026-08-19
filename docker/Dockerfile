FROM node:latest


# COPY . /home/app   for all data copy   also we used dockerignore file ingore the spacific folder that are actually not needed 
COPY index.js /home/app/index.js
COPY package.json /home/app/package.json


WORKDIR /home/app/


RUN npm install
EXPOSE 8000

CMD ["node","index"]
