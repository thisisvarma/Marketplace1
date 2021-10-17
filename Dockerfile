from python:3.8.6

RUN mkdir /code
workdir /code
copy . /code
run python -m pip install --upgrade pip
run pip install requirements.txt
