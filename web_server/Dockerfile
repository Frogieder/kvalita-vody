FROM python:3.10.4-alpine3.15
COPY app.py /usr/src/app/app.py
COPY set_iframes /usr/local/bin
WORKDIR /usr/src/app

# for debugging only - REMOVE (or at least comment out) for deployment
#RUN apk add --no-cache bash coreutils grep sed

RUN pip install --no-cache-dir -U flask waitress
ENTRYPOINT ["python"]
CMD ["app.py"]
