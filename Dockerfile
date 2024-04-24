FROM ubuntu
RUN apt-get install -y python3
WORKDIR /app
COPY util.py /app
CMD ["python", "utli.py"]