# base image  
FROM python:3.8-alpine
# setup environment variable  
ENV DockerHOME=/home/app/webapp  
ENV SECRET_KEY=django-insecure-*#3kq$q!bmd@=7!=&e!sxjsb1#g)t_q+)5yrh2k00s*f707r!l
ENV DATABASE_URL=postgres://b2bdb_user:z1aUKb0SjzBCmnErf2OvCEJTXEA69Rfn@dpg-cj5298c5kgrc73frc8i0-a.oregon-postgres.render.com/b2bdb
# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN apk add --update py-pip

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 0.0.0.0:8000