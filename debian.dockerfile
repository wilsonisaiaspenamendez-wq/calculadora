FROM debian:stable-slim
WORKDIR /debian/
COPY calculadora.deb /debian/
RUN apt-get update && apt-get install -y \
python3 \
python3-pip \
./calculadora.deb \
&& rm -rf /var/lib/apt/list/*
CMD ["/bin/bash"]