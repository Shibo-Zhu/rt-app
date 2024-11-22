import numpy as np
import time
# 将执行时间写入日志
import logging
import os

# 带上时间戳
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='task1.log')

# # 获取当前进程的 PID
# pid = os.getpid()

# # 设置进程仅运行在 CPU 核心 0 和 1 上
# os.sched_setaffinity(pid, {1})

# # 检查设置是否成功
# affinity = os.sched_getaffinity(pid)
# logging.info(f"进程 {pid} 绑定的 CPU 核心: {affinity}")


# 矩阵求逆
def matrix_inverse_task(size):
    start = time.time()
    for i in range(5):
        # 创建随机矩阵
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)
        C = np.random.rand(size, size)
        AT = np.linalg.inv(A)
        BT = np.linalg.inv(B)
        CT = np.linalg.inv(C)
        _ = AT * BT * CT
    end = time.time()

    logging.info(f"Matrix inverse took {end - start:.4f} seconds")

if __name__ == "__main__":

    size = 2000
    while True:
        matrix_inverse_task(size)
        time.sleep(1)
