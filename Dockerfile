FROM python:3.8.1

WORKDIR /martintest

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-dev \
        build-essential \
        libgdal-dev

RUN python -m pip install --upgrade pip

# RUN pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"

RUN rm -rf /var/lib/apt/lists/* && \
    useradd -ms /bin/bash martintest && \
    chown -R martintest:martintest ./

USER martintest

COPY --chown=martintest:martintest . ./

RUN PATH=$PATH:/home/martintest/.local/bin

RUN pip install --no-cache-dir --user -r requirements.txt

RUN rm requirements.txt
