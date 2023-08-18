FROM python:3.11.4

WORKDIR /usr/src/ideablog

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8005

RUN chmod +x /usr/src/ideablog/entrypoint.sh
ENTRYPOINT [ "/usr/src/ideablog/entrypoint.sh" ]
