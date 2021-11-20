FROM ubuntu:18.04
LABEL maintainer="Manjula Choudhary"

#use this to setup the system requirements
RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    git

RUN git clone --single-branch --branch master https://github.com/manjula18/fampay_youtube.git

ENV HOME /home/docker
WORKDIR ./fampay_youtube

RUN pip3 install -r requirements.text

#this is the command which will run the api to start the server
COPY docker_entry_cmd.sh $HOME/docker_entry_cmd.sh
RUN ["chmod", "+x", "/home/docker/docker_entry_cmd.sh"]
ENTRYPOINT ["/home/docker/docker_entry_cmd.sh"]



