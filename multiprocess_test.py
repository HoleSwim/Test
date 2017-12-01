# coding: utf8
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time
import Queue
import multiprocessing


def write(queue):
    for item in [1, 2, 3]:
        print('write: {}'.format(item))
        queue.put_nowait(item)
        time.sleep(1)
    queue.put_nowait('end')


def read(queue):
    while True:
        try:
            value = queue.get_nowait()
        except Queue.Empty:
            continue
        else:
            if value == 'end':
                break
            print('read: {}'.format(value))


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_list = []
    process_1 = multiprocessing.Process(target=write, args=(queue, ))
    process_list.append(process_1)
    process_2 = multiprocessing.Process(target=read, args=(queue, ))
    process_list.append(process_2)

    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
