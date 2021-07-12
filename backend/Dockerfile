FROM python:3.6.8
ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:${PATH}"
WORKDIR /blog
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./blog /blog
COPY ./scripts /scripts
