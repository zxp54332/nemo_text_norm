FROM python:3.8-slim-bullseye
ENV LANG C.UTF-8
RUN apt-get update

# Fix locale error
RUN apt-get install -y locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen
ENV LC_CTYPE en_US.UTF-8

WORKDIR /home/ubuntu/TextNorm
# Get project source code
COPY . .

# Build project
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r requirements.txt

EXPOSE 5252
CMD [ "bash", "script.sh"]
