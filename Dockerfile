# pull base image
FROM python:3.11.5-slim



# set working directory
WORKDIR /code



# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt



# copy project (everything to /app folder)
COPY . .


EXPOSE 80