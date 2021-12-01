# Build Docker image specific to CAP

FROM ml-base

COPY requirements.txt /opt/requirements.txt
WORKDIR /opt
RUN pip3 install -r requirements.txt