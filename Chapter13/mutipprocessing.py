from multiprocessing import Process, cpu_count
import time
import os


class MuchCPU(Process):
    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass


if __name__ == "__main__":
    procs = [MuchCPU() for f in range(cpu_count())]
    t = time.time()
    for p in procs:
        print("start")
        p.start()
    for p in procs:
        print("join")
        p.join()
    print(f"work took {time.time() - t} seconds")
