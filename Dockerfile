# Build Docker image specific to CAP

FROM ml-base
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /opt/requirements.txt
WORKDIR /opt
RUN pip3 install -r requirements.txt
