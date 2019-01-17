#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Python MultiProcessing - Watch a Process and restart it When fails
"""
from multiprocessing import Process
from time import sleep
import sys, os
import datetime


def task_1():
    print('{}: Sleep 5 seconds, Parent PID: {}, PID: {}'.format(sys._getframe().f_code.co_name, os.getppid(), os.getpid()))
    sleep(30)
    print('{}: Finished'.format(sys._getframe().f_code.co_name))
    sys.exit(0)


def task_2():
    print('{}: Sleep 5 seconds, Parent PID: {}, PID: {}'.format(sys._getframe().f_code.co_name, os.getppid(), os.getpid()))
    sleep(30)
    print('{}: Finished'.format(sys._getframe().f_code.co_name))
    sys.exit(0)


def allTasks(task):
    if task == 'task_1':
        return task_1()
    elif task == 'task_2':
        return task_2()
    else:
        pass


if __name__ == '__main__':
    tasks = ['task_1', 'task_2']
    processes = {}
    for task in tasks:
        p = Process(target=allTasks, args=(task,))
        p.start()
        processes[task] = (p, task)

    while len(processes) > 0:
        if datetime.datetime.now().minute >= 19:
            for key in processes.keys():
                p, task = processes[key]
                if p.is_alive():
                    p.terminate()
                    print('Termination {}'.format(task))
            print("Main Process exit!")
            break
        for key in processes.keys():
            p, task = processes[key]
            sleep(0.5)
            if not p.is_alive():  # Return whether the process is alive
                # not tunning
                print(task, 'is not alive')
                del processes[key]
                newP = Process(target=allTasks, args=(task,))
                newP.start()
                processes[task] = (newP, task)
            else:
                pass

    print('FINISHED')

"""
Multi-Threaded VS Multi-Process 
    Multi_Threaded:
        using shared memory space 
        Spawning processes is a bit slower than spawning threads 
        The threading library handles thread scheduling 
        threads share I/O scheduling -- which can be a bottleneck 
        
    Multi_Process:
        using separate memory
        the OS handles process scheduling.
        Processes have independent I/O scheduling 
    
    The GIL in cPython does not protect your program state, It protects the interpreter state.
        
"""