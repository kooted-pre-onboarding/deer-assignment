FROM python:3.8
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "deer.wsgi:application"]