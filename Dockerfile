FROM python:3.9.7-slim-buster
COPY . /bot
WORKDIR /bot
RUN pip3 install -r requirements.txt
CMD ["bash", "run.sh"]
