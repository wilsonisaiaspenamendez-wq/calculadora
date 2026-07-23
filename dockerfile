FROM python:alpine
WORKDIR /APP
COPY . /APP
RUN pip install --no-cache-dir numpy
CMD ["python", "calculadora.py"]
