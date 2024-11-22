import numpy as np
import time

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
        i = i + 1
        end = time.time()
        if flag:
            matrix_multiplication_task(100)
        else:
            busy_loop_task(iterations=10**5)
        if end - start > 10:
            flag = not flag
            if flag:
                print(f"Busy loop took {end - start:.4f} seconds, run {i} times")
                print("Starting matrix multiplication task")
            else:
                print(f"Matrix multiplication took {end - start:.4f} seconds, run {i} times")
                print("Starting busy loop task")
            start = time.time()
            i = 0
        
        
    # for i in range(100):  # 可以调整循环次数来控制任务的重复执行
        # print(f"\n--- Iteration {i+1} ---")
        
        # 执行缓存密集型任务（矩阵乘法）
        # print("Starting matrix multiplication task")
        # matrix_multiplication_task(size=500)  # 可以调整矩阵的大小来增加/减少负载

        # 执行简单任务（忙循环）
        # print("Starting busy loop task")
        # busy_loop_task(iterations=10**5)  # 可以调整循环次数来增加/减少负载

        # 睡眠一段时间，模拟任务之间的间隔
        # time.sleep(1)

# 运行任务
alternating_task()

