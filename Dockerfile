FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install libmagic1 libsndfile1 ffmpeg -y

RUN pip install --upgrade pip



RUN apt-get update



# ENTRYPOINT [ "service", "restart", ]
# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt 
RUN pip install bootstrap4

# RUN pip install -r requirements.txt --ignore-installed nose-progressive


# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000
# SHELL ["bash", "-c", "systemctl restart docker"]
