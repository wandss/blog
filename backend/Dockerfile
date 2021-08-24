#FROM python:3.6.8
FROM python:3.6.14-slim-bullseye
ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:${PATH}"
WORKDIR /blog
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./blog /blog
COPY ./scripts /scripts
RUN chmod a+x /scripts/entrypoint.sh
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["entrypoint.sh"]
