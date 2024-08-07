import os
from sys import argv
from multiprocessing import Process

rangeProcess = 1
rangeRequest = 1

target    = argv[1]
arguments = argv[2]

def getCommand():
    return f"curl -s -D - -o /dev/null {arguments} {target} | head -n 1"

def attack():
    for i in range(rangeRequest):
        os.system(getCommand())

lst_proc = []

for i in range(rangeProcess):
    procss = Process(target=attack, daemon=True)
    procss.start()
    lst_proc.append(procss)

for proc in lst_proc:
    if proc.is_alive():
        proc.join()
