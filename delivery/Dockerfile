FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /delivery
WORKDIR /delivery
ADD requirements.txt /delivery/
RUN pip install -r requirements.txt
ADD . /delivery/
