FROM ubuntu:18.04
LABEL maintainer="Manjula Choudhary"

#use this to setup the system requirements
RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    git

RUN git clone --single-branch --branch master https://github.com/manjula18/fampay_youtube.git

WORKDIR ./fampay_youtube

RUN pip3 install -r requirements.txt


#this is the command which will run the api to start the server
CMD python3 manage.py makemigrations
CMD python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000



