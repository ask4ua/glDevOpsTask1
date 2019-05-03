FROM python:3
RUN pip3 install psutil

VOLUME /app
ENTRYPOINT ["python3","/app/getres.py"]
CMD []

COPY ./app/ /app/
