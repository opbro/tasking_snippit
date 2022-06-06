import threading
from random import sample
from string import ascii_letters
from uuid import uuid4
import time

class YieldData(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = list()

    def run(self):
        for i in range(10):
            time.sleep(1)
            self.data.append("".join(sample(ascii_letters, k=20)))


def all_done(threads):
    for t_id in threads:
        if threads[t_id].is_alive():
            return False
    return True


def main():
    threads = {str(uuid4()): YieldData() for i in range(3)}
    for t_id in threads:
        threads[t_id].start()
        print(f'Started: {t_id}.')

    time.sleep(1)
    
    while True:
        for t_id in threads:
            print(f'Task Id: {t_id}: Results: {threads[t_id].data} .')
        print('='*4)
        if all_done(threads):
            break
    for t_id in list(threads.keys()):
            print(f'Task Id: {t_id}: Results: {len(threads[t_id].data)} .')
            del threads[t_id]
    pass


if __name__ == "__main__":
    main()
