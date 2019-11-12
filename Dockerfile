FROM ubuntu:16.04
MAINTAINER gabrielvie25@gmail.com
RUN apt-get update -qq && apt-get install -y \
wget \
openalpr \
openalpr-daemon \
openalpr-utils \
libopenalpr-dev \
git \
python3 \
python3-pip \
vim

RUN pip3 install pymysql opencv-python
RUN mkdir /app
WORKDIR /app
RUN git clone https://github.com/GabrieelV/leitorplacas.git
RUN cp /app/leitorplacas/executar.py /app
RUN rm -rf /app/leitorplacas
