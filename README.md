# Calcu
A Web based calculator for finite integers.

## Backend

First navigating to the root directory, then type the following commands
```
export FLASK_APP=backend/app.py
flask run
```

## Frontend

First navigating to the frontend directory, then type the following commands
```
npm install # install dependencies, need to run only once 
npm start
```

## docker (untested, since my PC is out of disk)

The simplest way to start both backend/frontend. Need to install `docker`, and `docker-compose` to build, and run services.
```
docker-compose build
docker-compose run
```
