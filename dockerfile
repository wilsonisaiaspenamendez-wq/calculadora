FROM python:3.13.5-slim
WORKDIR /APP
COPY . /APP
CMD [ "python", "import ladrillos.py" ]
