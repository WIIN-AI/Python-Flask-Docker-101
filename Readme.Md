
## Docker 101 (File & Commands)

####   Docker FIle 
- FROM python:3.6
- MAINTAINER Vinaykumar Puppala "Vinaykumar.puppala@outlook.com"
- COPY . /app
- WORKDIR /app
- RUN pip install -r requirements.txt
- ENTRYPOINT ["python"]
- CMD ["app.py"]

####  Docker Commands

- docker build --tag python-docker .
- docker images
- docker tag python-docker:latest python-docker:v1.0.0
- docker rmi python-docker:v1:0.0
- docker run python-docker
- docker run --publish 5000:5000 python-docker
- docker run -d -p 5000:5000 python-docker #detached mode
- docker stop <Name>