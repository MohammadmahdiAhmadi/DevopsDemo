##
# pull official base image
##
FROM python:3.11.4-slim-buster

##
# set work directory
##
WORKDIR /usr/src/ideablog

##
# set environment variables
##
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

##
# install dependencies
##
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

##
# copy project
##
COPY . .



# FROM python:3.7.5
# RUN mkdir /ideablog
# WORKDIR /ideablog
# COPY . /ideablog
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# ADD . /ideablog
# EXPOSE 8005
# # CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]
# CMD ["gunicorn", "--chdir", "ideablog", "--bind", ":8005", "--timeout", "300",  "ideablog.wsgi:application"]
