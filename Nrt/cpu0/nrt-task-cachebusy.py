import numpy as np
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='NRT-task-toggle.log')

def matrix_multiplication_task(size):
    start = time.time()
    for i in range(5):
        # 创建两个随机矩阵
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)
        C = np.dot(A, B)
    end = time.time()
    # print(f"Matrix multiplication took {end - start:.4f} seconds")

def busy_loop_task(iterations):
    # 简单的忙等待循环
    start = time.time()
    count = 0
    for _ in range(iterations):
        count += 1
    end = time.time()
    # print(f"Busy loop took {end - start:.4f} seconds")

def alternating_task():
    start = time.time()
    flag = True
    i = 0
    while True:
    	time.sleep(0.01)
        i = i + 1
        end = time.time()
    	matrix_multiplication_task(2000)
        if end - start > 10:

	    logging.info(f"Matrix multiplication took {end - start:.4f} seconds, run {i} times")
            start = time.time()
            i = 0
        

# 运行任务
alternating_task()

