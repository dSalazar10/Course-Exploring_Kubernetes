FROM ubuntu:16.04
WORKDIR /app
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update && apt-get install -y tidy
COPY . /app
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]