import threading
import time

counter = 0
lock = threading.Lock()

def trythis():
    global counter
    with lock:
        counter += 1
        print(f"Job {counter} has started")
        
    # Simulate some work
    time.sleep(1)
    
    with lock:
        print(f"Job {counter} has finished")
        counter -= 1

threads = []
for _ in range(2):
    t = threading.Thread(target=trythis)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

