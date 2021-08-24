#FROM python:3.6.8
FROM python:3.6.14-slim-bullseye
ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:${PATH}"
ENV PORT=8000
COPY ./requirements.txt /requirements.txt
COPY ./blog /blog
COPY ./scripts /scripts
RUN pip install -r /requirements.txt
RUN groupadd -rf -g 1001 django && \
    useradd -r -M -g 1001 -u 1001 django && \
    chown -R django:django /scripts && \
    chown -R django:django /blog && \
    chmod a+x /scripts/entrypoint.sh
USER django
WORKDIR /blog
EXPOSE ${PORT}
CMD ["python", "manage.py", "runserver", "0.0.0.0:${PORT}"]
#CMD ["entrypoint.sh"]
