FROM ubuntu:22.04

##################
# OS dependencies
##################

RUN apt update && apt-get update
RUN apt-get install -y python3 python3-pip git wget zip

RUN cp /usr/bin/python3 /usr/bin/python

###################
# Setup App
###################

WORKDIR /app

RUN pip install -U pip

RUN git clone https://github.com/pytorch/fairseq
WORKDIR /app/fairseq
RUN pip install --editable ./

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN bash install_sctk.sh

# WORKDIR /app/data
# RUN wget https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
# RUN python -m wikiextractor.WikiExtractor zhwiki-latest-pages-articles.xml.bz2
# RUN rm zhwiki-latest-pages-articles.xml.bz2

WORKDIR /app

CMD while :; do sleep 100; done
