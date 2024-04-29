import threading
import time
import queue

max_items = 5
q = queue.Queue(max_items)

def producer():
    for i in range(max_items):
        item = f"Item {i+1}"
        q.put(item)
        print(f"Produced {item}")
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        if item is None:  # Break the loop when all items are consumed
            break
        print(f"Consumed {item}")
        time.sleep(2)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Signal the consumer to exit after all items are consumed
consumer_thread.join()

