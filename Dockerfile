FROM python:3.12.3

WORKDIR /usr/src/app

#ENV PYTHONUNBUFFERED 0

COPY requirements.txt /tmp/pip-tmp/

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

COPY . .

CMD ["python", "src/main.py"]

