FROM m.daocloud.io/docker.io/library/python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install numpy
CMD ["chrt", "-d", "--sched-runtime", "9500000", "--sched-deadline", "10000000", "--sched-period", "10000000", "0", "python", "task1.py"]
