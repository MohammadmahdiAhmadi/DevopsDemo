FROM python:3.7.5
RUN mkdir /ideablog
WORKDIR /ideablog
COPY . /ideablog
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /ideablog
EXPOSE 8005
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]
CMD ["gunicorn", "--chdir", "ideablog", "--bind", ":8005", "--timeout", "300",  "ideablog.wsgi:application"]

