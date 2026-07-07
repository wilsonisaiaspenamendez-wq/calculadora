FROM python:3.13.5-slim
WORKDIR /APP
COPY . /APP
RUN pip install --no-cache-dir numpy
CMD ["python", "Calculadora.py"]
