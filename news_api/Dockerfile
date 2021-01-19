FROM python:3.8.3

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY app/ /usr/src/app
COPY entrypoint.sh /usr/src/app
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

