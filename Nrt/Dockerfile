FROM m.daocloud.io/docker.io/library/python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install numpy
CMD ["python", "nrt-task-cachebusy.py"]

